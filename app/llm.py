import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(query: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an AI document assistant.

Answer the user's question using ONLY the context below.
If the answer is not found in the context, say:
"I could not find that information in the uploaded document."

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

def generate_non_grounded_answer(query: str) -> str:

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content