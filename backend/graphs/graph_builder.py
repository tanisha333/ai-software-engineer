from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from graphs.state import AgentState
from graphs.nodes.software_engineer import software_engineer

from tools.file_tool import read_file
from tools.search_tool import search_code
from tools.directory_tool import list_directory
from tools.retriever_tool import retrieve_code
from tools.write_file import write_file
from tools.create_file import create_file

from graphs.checkpointer import memory


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("software_engineer", software_engineer)

    graph.add_node(
        "tools",
        ToolNode([
            read_file,
            search_code,
            list_directory,
            retrieve_code,
            write_file,
            create_file,
        ])
    )

    graph.add_edge(START, "software_engineer")

    graph.add_conditional_edges(
        "software_engineer",
        tools_condition,
    )

    graph.add_edge("tools", "software_engineer")

    return graph.compile(checkpointer=memory)