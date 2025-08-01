from modules.groq_client import ask_llm_groq
from modules.embedding_store import EmbeddingStore

query = "What is a jailbreak prompt?"
store = EmbeddingStore()
top_chunks = store.search(query, k=5)

context = "\n\n".join([c["chunk"] for c in top_chunks])
response = ask_llm_groq(query, context)

print("💬 LLM Answer:\n")
print(response)
