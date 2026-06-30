# 📚 RAG ChromaDB

A simple Retrieval-Augmented Generation (RAG) project that demonstrates how to load a PDF, split it into text chunks, generate embeddings using Google Gemini, and store those embeddings in a ChromaDB vector database.

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split text into chunks
- 🧠 Generate embeddings using Google Gemini
- 💾 Store embeddings in ChromaDB
- ⚡ Fast vector database creation
- 🏗️ Foundation for building AI PDF Chatbots

---

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini Embeddings
- ChromaDB
- PyPDF
- Python-dotenv

---

## 📂 Project Structure

```text
17-RAG-ChromaDB/
│
├── app.py
├── sample.pdf
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── chroma_db/
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/adilali48/AI-Portfolio.git
```

### 2️⃣ Go to the project folder

```bash
cd 17-RAG-ChromaDB
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Google Gemini API key.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📋 Example Output

```text
Total Pages: 36
Total Chunks: 75

✅ ChromaDB Created Successfully!
Stored Chunks: 75
```

---

## 🧠 How It Works

```
PDF
 │
 ▼
Load PDF
 │
 ▼
Split into Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store in ChromaDB
```

---

## 📦 Dependencies

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

After completing this project, you will understand:

- How RAG stores document embeddings
- What a Vector Database is
- How ChromaDB works
- How embeddings are generated using Google Gemini
- How modern AI applications prepare data for semantic search

---

## 🚀 Next Project

➡️ **Project 18 – RAG Similarity Search**

In the next project, users will ask questions, and ChromaDB will retrieve the most relevant chunks from the PDF.

---

## 👨‍💻 Author

**Adil Ali**

- 🌍 Pakistan
- 💼 AI & Python Developer
- 🐙 GitHub: https://github.com/adilali48
- 💼 LinkedIn: https://linkedin.com/in/adil-ali-a28989285

---

⭐ If you found this project helpful, don't forget to star the repository!