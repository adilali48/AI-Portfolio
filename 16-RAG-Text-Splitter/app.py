from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print(f"Pages: {len(documents)}")

# Split Text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"\nTotal Chunks: {len(chunks)}")

print("\n========== FIRST CHUNK ==========\n")

print(chunks[0].page_content) 