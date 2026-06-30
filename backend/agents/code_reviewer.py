from prompts.code_reviewer import code_review_prompt
from utils.llm import get_llm

llm = get_llm()

chain = code_review_prompt | llm


def review_code(code: str):

    response = chain.invoke(
        {
            "code": code
        }
    )

    return response.content