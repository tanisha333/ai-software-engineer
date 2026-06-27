from prompts.software_engineer import software_engineer_prompt
from utils.llm import get_llm
from tools.file_tool import read_file
from tools.search_tool import search_code
from tools.directory_tool import list_directory


llm = get_llm().bind_tools([read_file,search_code,list_directory,])
chain = software_engineer_prompt | llm


def software_engineer(state):
    response = llm.invoke("messages":state["messages"])

    return {
        "messages": [response]
    }