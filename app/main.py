from fastapi import FastAPI, UploadFile, File
from app.document_loader import extract_text_from_pdf
from app.chunker import chunk_text
from app.embeddings import create_embeddings, model
from app.vector_store import VectorStore
from app.llm import generate_answer

app = FastAPI()

vector_store = None

@app.get("/")
def root():
    return {"message": "AI Document Assistant Backend Running"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    global vector_store

    file_bytes = await file.read()

    extracted_text = extract_text_from_pdf(file_bytes)

    chunks = chunk_text(extracted_text)

    embeddings = create_embeddings(chunks)

    embedding_dimension = embeddings.shape[1]

    vector_store = VectorStore(embedding_dimension)

    vector_store.add_embeddings(embeddings, chunks)

    return {
        "filename": file.filename,
        "number_of_chunks": len(chunks),
        "embedding_dimension": embedding_dimension,
        "message": "Document processed and stored successfully"
    }

@app.get("/search")
def search(query: str):
    global vector_store

    if vector_store is None:
        return {"error": "No document uploaded"}

    query_embedding = model.encode(query)

    results = vector_store.search(query_embedding)

    return {
        "query": query,
        "results": results
    }

@app.get("/ask")
def ask(query: str):
    global vector_store

    if vector_store is None:
        return {"error": "No document uploaded"}

    query_embedding = model.encode(query)

    retrieved_chunks = vector_store.search(query_embedding)

    answer = generate_answer(query, retrieved_chunks)

    return {
        "query": query,
        "answer": answer,
        "sources": retrieved_chunks
    }