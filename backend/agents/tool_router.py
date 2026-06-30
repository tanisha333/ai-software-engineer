from prompts.tool_router import tool_router_prompt
from utils.llm import get_llm

llm = get_llm()

chain = tool_router_prompt | llm


def choose_tool(question: str):

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content.strip()