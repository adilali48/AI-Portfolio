import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_chroma import Chroma

# Load API Key
load_dotenv()

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split PDF into Chunks
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

# Create ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="chroma_db"
)

print("✅ RAG Chatbot Ready!")

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

while True:

    question = input("\nAsk a Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye 👋")
        break

    # Retrieve top 3 relevant chunks
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an AI assistant.

Answer ONLY using the information provided in the context below.

If the answer is not available in the context, reply:
"I couldn't find that information in the provided PDF."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\n==============================")
    print("AI Answer:\n")
    print(response.content)