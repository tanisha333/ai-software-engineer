from prompts.software_engineer import software_engineer_prompt
from utils.llm import get_llm

from tools.file_tool import read_file
from tools.search_tool import search_code
from tools.directory_tool import list_directory
from tools.retriever_tool import retrieve_code
from tools.write_file import write_file
from tools.create_file import create_file


llm = get_llm().bind_tools(
    [
        read_file,
        search_code,
        list_directory,
        retrieve_code,
        write_file,
        create_file,
    ]
)

# Prompt → LLM
chain = software_engineer_prompt | llm


def software_engineer(state):

    response = chain.invoke(
        {
            "messages": state["messages"]
        }
    )

    return {
        "messages": [response]
    }