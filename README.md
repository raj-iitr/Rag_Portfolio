# Rag_Portfolio
# RAG Portfolio App

A fully local-first, free Retrieval-Augmented Generation (RAG) system that lets you upload documents (PDF, DOCX, PPTX, XLSX, MD), semantically search them, and chat with an LLM (via Groq API) over their content.

---

## 🔧 Features

* ✅ Upload multi-format documents
* ✅ Extract, chunk, and embed using MiniLM
* ✅ Store embeddings in local FAISS vector DB
* ✅ Chat UI with memory and streaming responses
* ✅ LLM-powered Q\&A via Groq (e.g., gemma2-9b-instruct)
* ✅ No cloud storage or paid components required

---

## 📦 Tech Stack

| Layer      | Tool                           |
| ---------- | ------------------------------ |
| UI         | Streamlit                      |
| Backend    | Python                         |
| Extractors | pdfplumber, python-docx, etc.  |
| Chunking   | LangChain                      |
| Embedding  | sentence-transformers (MiniLM) |
| Vector DB  | FAISS                          |
| LLM        | Groq API (OpenAI-compatible)   |

---

## 📁 Project Structure

```
rag-portfolio-app/
├── app.py                 # Streamlit app
├── .env                  # Groq API key + model
├── documents/            # Uploaded files
├── vector.index          # FAISS index (persisted)
├── meta.pkl              # Chunk metadata (persisted)
├── modules/
│   ├── parser.py         # File extractors
│   ├── chunker.py        # Text chunker
│   ├── embedding_store.py# VectorDB manager
│   └── groq_client.py    # LLM call logic
└── requirements.txt
```

---

## ⚙️ Setup Instructions

```bash
# 1. Clone & enter project folder
$ git clone <repo-url> && cd rag-portfolio-app

# 2. Create and activate virtual env
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Add your Groq credentials to `.env`
GROQ_API_KEY=sk-xxx
GROQ_MODEL=gemma2-9b-instruct

# 5. Launch app
$ streamlit run app.py
```

---

## 💬 How It Works

1. Upload one or more supported documents
2. They're parsed → chunked → embedded → stored in FAISS
3. Ask a question in the chat
4. Top-k matching chunks retrieved
5. Query + history + context sent to Groq LLM
6. Answer returned and shown in chat with memory

---

## 🧠 Advanced Features

* 🔄 Persistent vector store (`vector.index`, `meta.pkl`)
* 💬 Conversational memory via `st.session_state`
* 📌 Prompt combines history + document context
* ⚡ Supports multi-doc queries seamlessly
* 🔐 .env-based secrets management

---

## 🔒 Security / Limitations

* No real-time Notion sync (manual .md only)
* No user login/session isolation (MVP)
* Chat not persisted unless you add a DB or `.json` log

---

## 👨‍💻 Author

Built with ❤️ by Rajarshi

---

## ✨ Sample Prompt (to LLM)

```text
You are an assistant. Use the following conversation history and document context to answer the question:

Conversation History:
User: What is a jailbreak prompt?
Assistant: A prompt that bypasses the safeguards of an LLM...

Retrieved Document Context:
...

Current Question:
How do jailbreak prompts evolve over time?

Answer:
```

---
