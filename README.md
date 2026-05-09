# AI Document Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload technical documents and ask grounded questions over the document contents using semantic retrieval and LLM-based response generation.

## Features

- PDF document upload and parsing
- Semantic chunking and retrieval pipeline
- Embedding generation using sentence-transformers
- FAISS vector database integration
- Grounded response generation using OpenAI API
- FastAPI backend with Swagger UI
- Dockerized deployment environment

---

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI / Machine Learning
- OpenAI API
- Sentence Transformers
- PyTorch
- FAISS
- Scikit-learn ecosystem

### Infrastructure / DevOps
- Docker
- Git
- GitHub

---

## System Architecture

```text
User Query
    ↓
FAISS Semantic Retrieval
    ↓
Relevant Document Chunks
    ↓
LLM Prompt Construction
    ↓
OpenAI Response Generation
    ↓
Grounded Answer
```

---

## API Endpoints

### Upload Document

```http
POST /upload
```

Uploads and processes PDF documents into embeddings stored in FAISS.

### Ask Questions

```http
GET /ask?query=...
```

Retrieves relevant chunks and generates grounded responses using OpenAI.

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/nadia-jahan/ai-document-assistant.git
cd ai-document-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Running with Docker

### Build Docker Image

```bash
docker build -t ai-document-assistant .
```

### Run Container

```bash
docker run -p 8000:8000 --env-file .env ai-document-assistant
```

---

## Future Improvements

- Multi-document support
- Persistent vector storage
- Frontend interface
- Cloud deployment with GCP Cloud Run
- Kubernetes orchestration
- Advanced chunking strategies

---

## Author
Nadia Jahan