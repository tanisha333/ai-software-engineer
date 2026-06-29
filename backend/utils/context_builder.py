from langchain_core.documents import Document


def build_context(documents: list[Document]) -> str:

    context = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown File"
        )

        context.append(
            f"""
File:
{source}

Code:
{document.page_content}
"""
        )

    return "\n\n".join(context)