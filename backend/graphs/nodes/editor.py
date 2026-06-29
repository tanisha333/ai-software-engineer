from prompts.code_editor import code_editor_prompt
from utils.llm import get_llm

llm = get_llm()

chain = code_editor_prompt | llm


def editor(state):

    response = chain.invoke(
        {
            "input": state["messages"][-1].content
        }
    )

    return {
        "messages": [response]
    }