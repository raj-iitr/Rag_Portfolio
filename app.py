# app.py
import os
import streamlit as st
from modules.parser import extract_text
from modules.chunker import chunk_text
from modules.embedding_store import EmbeddingStore
from modules.groq_client import ask_llm_groq

UPLOAD_DIR = "documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)

store = EmbeddingStore()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.subheader("💬 Chat with Your Documents")


st.set_page_config(page_title="RAG Portfolio App", layout="wide")
st.title("📄 RAG Portfolio App")

# File Upload UI
uploaded_files = st.file_uploader(
    "Upload documents (PDF, DOCX, PPTX, XLSX, MD)",
    type=["pdf", "docx", "pptx", "xlsx", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    st.subheader("📁 Uploaded Files")

    for file in uploaded_files:
        save_path = os.path.join(UPLOAD_DIR, file.name)
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        file_size_kb = round(len(file.getvalue()) / 1024, 2)
        st.markdown(f"- **{file.name}** ({file_size_kb} KB)")

        # Extract → Chunk → Embed
        with st.spinner(f"Processing {file.name}..."):
            raw_text = extract_text(save_path)
            chunks = chunk_text(raw_text)
            store.add(chunks, file_id=file.name)

    st.success("All files embedded into vector DB.")

# Query Input UI
user_input = st.chat_input("Ask something about the uploaded documents...")

if user_input:
    with st.spinner("Thinking..."):
        top_chunks = store.search(user_input, k=2)
        context = "\n\n".join([c["chunk"] for c in top_chunks])
        response = ask_llm_groq(user_input, context)


    # Save interaction
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display entire chat history
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])