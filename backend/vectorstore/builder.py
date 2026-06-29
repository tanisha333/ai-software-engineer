from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv

load_dotenv()
import os

print(os.getenv("GOOGLE_API_KEY"))

from config.settings import (
    CHROMA_DB_PATH,
    EMBEDDING_MODEL,
)

from vectorstore.loader import load_project
from vectorstore.splitter import split_documents


def build_vector_store():

    print("Loading project...")

    documents = load_project()

    print(f"Loaded {len(documents)} documents.")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings...")

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH,
    )

    print("Vector database created successfully!")

if __name__ == "__main__":
    build_vector_store()
