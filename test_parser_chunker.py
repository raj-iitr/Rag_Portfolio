from modules.parser import extract_text
from modules.chunker import chunk_text


doc_path = "C:/Users/Dell/Desktop/ML/rag-portfolio-app/documents/dan.pdf"  # Replace with an actual file you uploaded
raw_text = extract_text(doc_path)
chunks = chunk_text(raw_text)

print(f"✅ Extracted {len(chunks)} chunks")
print("🧩 First 2 chunks:\n")
for chunk in chunks[:2]:
    print(chunk)
    print("-" * 50)

