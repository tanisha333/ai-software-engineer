from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from graph.state import AgentState
from graph.nodes import software_engineer
from tools.file_tool import read_file
from tools.search_tool import search_code
from tools.directory_tool import list_directory
from graph.checkpointer import memory



def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("software_engineer",software_engineer)
    graph.add_node("planner",planner)

    graph.add_node("tools",ToolNode([read_file,search_code,list_directory,]))

    graph.add_edge(START,"planner")
    graph.add_conditional_edges(
    "software_engineer",
    tools_condition,
    )

    # graph.add_edge("software_engineer",END)
    graph.add_edge("tools","software_engineer")
    graph.add_edge("planner","software_engineer")



    app = graph.compile(checkpointer=memory)

    return app