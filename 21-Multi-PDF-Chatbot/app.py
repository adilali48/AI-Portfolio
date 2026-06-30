import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_chroma import Chroma

# Load API Key
load_dotenv()

# Streamlit Page Config
st.set_page_config(
    page_title="Multi PDF AI Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Multi PDF AI Chatbot")
st.write("Upload multiple PDFs and ask questions!")

# Upload Multiple PDFs
uploaded_files = st.file_uploader(
    "📄 Upload PDF Files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    all_documents = []

    # Read all uploaded PDFs
    for pdf in uploaded_files:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf.read())
            pdf_path = tmp.name

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        all_documents.extend(documents)

    st.success(f"✅ Total PDFs Uploaded: {len(uploaded_files)}")
    st.info(f"📄 Total Pages Loaded: {len(all_documents)}")

    # Split Documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(all_documents)

    st.info(f"🧩 Total Chunks: {len(chunks)}")

    # Embedding Model
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    # Create ChromaDB
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    st.success("✅ ChromaDB Created Successfully!")

    # Ask Question
    question = st.text_input("💬 Ask a Question")

    if question:

        docs = db.similarity_search(question, k=3)

        context = "\n\n".join(doc.page_content for doc in docs)

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3,
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer is not available in the context, reply:

"I couldn't find that information in the uploaded PDFs."

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        st.subheader("🤖 AI Answer")
        st.write(response.content)