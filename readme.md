# 📄 PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload a PDF and ask questions about its content. The system processes the document, creates embeddings, stores them in a vector database, and retrieves relevant context to generate accurate answers.

---

## 🚀 Features

* Upload and process PDF documents
* Intelligent document chunking
* Vector similarity search for relevant context
* Retrieval-Augmented Generation (RAG)
* Interactive web interface
* Fast API backend for scalable architecture

---

## 🧠 Architecture

User Interface → API → Document Processing → Vector Database → Retrieval → LLM Response

**Workflow**

1. User uploads a PDF
2. Document is split into chunks
3. Embeddings are generated
4. Chunks are stored in a vector database
5. User asks a question
6. Relevant chunks are retrieved
7. LLM generates an answer using retrieved context

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Streamlit
* LangGraph
* FAISS (Vector Database)
* HuggingFace Embeddings
* Groq LLM (Llama 3.1)

---

## 📂 Project Structure

```
project/
│
├── api.py            # FastAPI server
├── main.py           # RAG pipeline + LangGraph workflow
├── app.py            # Streamlit interface
├── uploaded.pdf      # Uploaded document
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

Create a virtual environment

```
python -m venv venv
```

Activate the environment

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

### Start FastAPI Server

```
uvicorn api:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

### Start Streamlit App

```
streamlit run app.py
```

Streamlit UI will open in your browser.

---

## 💬 How to Use

1. Upload a PDF using the interface
2. The system processes the document
3. Ask questions related to the PDF
4. The chatbot retrieves relevant information and generates answers

---

## 📌 Example Use Cases

* Research paper Q&A
* Legal document exploration
* Study material assistant
* Knowledge base chatbot

---

## 🔮 Future Improvements

* Multi-PDF support
* Chat history memory
* Streaming responses
* Hybrid search (BM25 + vector search)
* Document highlighting

---

## 📜 License

This project is for educational and research purposes.

---

## 👨‍💻 Author

Built by **Piyush Tiwari**

AI / Data Science Enthusiast
