import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

class EmbeddingStore:
    def __init__(self, index_path="vector.index", meta_path="meta.pkl"):
        self.index_path = index_path
        self.meta_path = meta_path
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.metadata = []

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.load()
        else:
            self.index = faiss.IndexFlatL2(384)
            self.metadata = []

    def add(self, chunks: list[str], file_id: str):
        embeddings = self.model.encode(chunks)
        self.index.add(embeddings)
        self.metadata.extend([
            {"file": file_id, "chunk": text} for text in chunks
        ])
        self.save()

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.meta_path, "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query: str, k=5):
        query_vec = self.model.encode([query])
        D, I = self.index.search(query_vec, k)
        return [self.metadata[i] for i in I[0]]

print("EmbeddingStore module loaded successfully.")