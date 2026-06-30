# 🤖 AI PDF Chatbot

A professional AI-powered PDF Chatbot built using **Streamlit**, **LangChain**, **Google Gemini**, and **ChromaDB**. Upload a PDF, ask questions in natural language, and receive intelligent answers generated from the document.

---

## 🚀 Features

- 📄 Upload PDF files
- 📚 Automatic PDF text extraction
- ✂️ Smart text chunking
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
20-AI-PDF-Chatbot/
│
├── app.py
├── sample.pdf
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
cd 20-AI-PDF-Chatbot
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

The application will open automatically in your browser.

---

## 🧠 How It Works

```
Upload PDF
      │
      ▼
Read PDF
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

- Retrieval-Augmented Generation (RAG)
- Vector Databases (ChromaDB)
- Google Gemini Integration
- Semantic Search
- Streamlit Web Applications
- AI-powered Question Answering

---

## 📸 Demo

1. Upload a PDF.
2. Ask a question about the document.
3. Receive an AI-generated answer based on the uploaded PDF.

---

## 🚀 Future Improvements

- 📄 Multiple PDF Upload
- 💬 Chat History
- 🌙 Dark/Light Theme
- 📝 Conversation Memory
- 📥 Download Chat History
- ☁️ Cloud Deployment

---

## 👨‍💻 Author

**Adil Ali**

- 🐙 GitHub: https://github.com/adilali48
- 💼 LinkedIn: https://linkedin.com/in/adil-ali-a28989285

---

## ⭐ Support

If you found this project helpful, please consider giving the repository a ⭐ on GitHub.

Happy Coding! 🚀