from prompts.planner import planner_prompt
from utils.llm import get_llm

llm = get_llm()
chain = planner_prompt | llm


def planner(state):

    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }