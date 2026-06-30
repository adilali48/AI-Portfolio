# 📚 Multi PDF AI Chatbot

An AI-powered chatbot that allows users to upload **multiple PDF documents** and ask questions across all uploaded files. Built using **Streamlit**, **LangChain**, **Google Gemini**, and **ChromaDB**.

---

## 🚀 Features

- 📄 Upload multiple PDF files
- 📚 Read and combine multiple documents
- ✂️ Automatic text chunking
- 🧠 Google Gemini Embeddings
- 💾 ChromaDB Vector Database
- 🔍 Semantic Similarity Search
- 🤖 AI-powered answers using Gemini
- 🌐 Interactive Streamlit Web Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- ChromaDB
- PyPDF
- Python-dotenv

---

## 📂 Project Structure

```text
21-Multi-PDF-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── chroma_db/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/adilali48/AI-Portfolio.git
```

### 2. Navigate to the Project

```bash
cd 21-Multi-PDF-Chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project folder and add your Gemini API key.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 🧠 How It Works

```
Upload Multiple PDFs
          │
          ▼
Read All PDFs
          │
          ▼
Merge Documents
          │
          ▼
Split into Chunks
          │
          ▼
Generate Embeddings
          │
          ▼
Store in ChromaDB
          │
          ▼
Similarity Search
          │
          ▼
Gemini AI
          │
          ▼
Answer User Questions
```

---

## 📦 Required Packages

- streamlit
- langchain
- langchain-community
- langchain-google-genai
- langchain-text-splitters
- langchain-chroma
- chromadb
- pypdf
- python-dotenv

---

## 🎯 Learning Outcomes

This project demonstrates:

- Multi-document Retrieval-Augmented Generation (RAG)
- Google Gemini Embeddings
- ChromaDB Vector Database
- Semantic Search
- Streamlit Web Applications
- AI-powered Question Answering
- Multi-file Document Processing

---

## 📸 Demo

1. Upload multiple PDF files.
2. Ask a question related to any uploaded document.
3. The chatbot searches across all PDFs.
4. Receive an AI-generated answer based on the combined knowledge.

---

## 🚀 Future Improvements

- 💬 Chat History
- 📄 Source Citation
- 🌙 Dark/Light Theme
- ⚡ Cached Vector Database
- 📥 Download Chat
- ☁️ Cloud Deployment
- 🧠 Conversation Memory

---

## 👨‍💻 Author

**Adil Ali**

- 🐙 GitHub: https://github.com/adilali48
- 💼 LinkedIn: https://linkedin.com/in/adil-ali-a28989285

---

## ⭐ Support

If you found this project useful, please give the repository a ⭐ on GitHub.

Happy Coding! 🚀