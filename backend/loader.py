from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.document_loaders import DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os
import shutil

CHROMA_PATH = "database"
DATA_PATH = "data"

def load_documents():
    # Load all documents from the data folder.
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf")
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    # Split documents into chunks for RAG processing.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

def to_Chroma(chunks: list[Document]):
    # Clear the previous database if it exists
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Obtain embeddings
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create a new database from documents
    db = Chroma.from_documents(
        documents=chunks, embedding=embedding_function, persist_directory=CHROMA_PATH
    )
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def setup_database():
    documents = load_documents()
    chunks = split_text(documents)
    to_Chroma(chunks)

if __name__ == "__main__":
    setup_database()
