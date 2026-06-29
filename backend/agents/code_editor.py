from prompts.code_editor import code_editor_prompt
from utils.llm import get_llm

llm = get_llm()

chain = code_editor_prompt | llm


def edit_code(
    original_code: str,
    request: str,
):

    prompt = f"""
Original Code

{original_code}

-------------------------

User Request

{request}
"""

    return chain.invoke(
        {
            "input": prompt
        }
    ).content