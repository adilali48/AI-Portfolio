import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load Environment Variables
load_dotenv()

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print(f"Total Pages: {len(documents)}")

# Split PDF
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

# Create Embedding Model
embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Create ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="chroma_db"
)

print("\n✅ ChromaDB Created Successfully!")

print(f"Stored Chunks: {db._collection.count()}")