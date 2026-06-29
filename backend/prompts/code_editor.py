from langchain_core.prompts import ChatPromptTemplate

code_editor_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Software Engineer.

You receive:

• Original source code

• User request

Return ONLY the updated source code.

Never explain.

Never use markdown.

Return executable code only.
"""
        ),
        (
            "human",
            "{input}"
        )
    ]
)