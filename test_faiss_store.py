from modules.parser import extract_text
from modules.chunker import chunk_text
from modules.embedding_store import EmbeddingStore

doc_path = "C:/Users/Dell/Desktop/ML/rag-portfolio-app/documents/dan.pdf"
raw = extract_text(doc_path)
chunks = chunk_text(raw)

store = EmbeddingStore()
store.add(chunks, file_id="sample.pdf")

results = store.search("What is a jailbreak prompt?")
print("🔍 Top Matches:\n")
for match in results:
    print(match["chunk"])
    print("-" * 40)
