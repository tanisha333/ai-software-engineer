from vectorstore.retriever import retrieve

from utils.llm import get_llm

llm = get_llm()


def explain_project(question: str):

    docs = retrieve(question)

    context = ""

    for doc in docs:

        context += f"""

File:
{doc.metadata.get("source")}

Code:

{doc.page_content}

"""

    prompt = f"""
You are an expert Software Engineer.

Answer the user's question using ONLY the project context.

Project Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    return response.content