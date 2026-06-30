import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load API Key
load_dotenv()

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split PDF
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

# Embedding Model
embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Create Vector Database
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="chroma_db"
)

print("✅ ChromaDB Ready!")

# Ask User Question
question = input("\nAsk a Question: ")

# Search Similar Chunks
results = db.similarity_search(question, k=3)

print("\n========== TOP 3 RESULTS ==========\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}")
    print("-" * 50)
    print(doc.page_content)
    print()