import os
import openai
from dotenv import load_dotenv
load_dotenv()

# ⚠️ Set your Groq API key here or via env var
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"
GROQ_MODEL = os.getenv("GROQ_MODEL", "compound-beta")

def ask_llm_groq(query: str, context: str) -> str:
    prompt = f"""You are an assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""

    response = openai.ChatCompletion.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=512
    )

    return response.choices[0].message["content"].strip()
