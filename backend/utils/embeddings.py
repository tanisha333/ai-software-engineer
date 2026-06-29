import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config.settings import EMBEDDING_MODEL

load_dotenv()


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )