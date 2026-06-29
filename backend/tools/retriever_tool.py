from langchain_core.tools import tool

from vectorstore.retriever import retrieve
from utils.context_builder import build_context


@tool
def retrieve_code(question: str) -> str:
    """
    Retrieve relevant code from the project.
    """

    docs = retrieve(question)

    return build_context(docs)