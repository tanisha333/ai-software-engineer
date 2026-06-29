from dotenv import load_dotenv
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from config.settings import (
    CHROMA_DB_PATH,
    EMBEDDING_MODEL,
)

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

vector_store = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=embeddings,
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


def retrieve(question: str):
    return retriever.invoke(question)


if __name__ == "__main__":

    docs = retrieve("Gemini")

    for doc in docs:
        print("=" * 60)
        print(doc.metadata)
        print(doc.page_content[:500])