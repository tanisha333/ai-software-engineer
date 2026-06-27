from langchain_core.tools import tool


@tool
def read_file(file_path: str) -> str:
    """ Read the contents of a file."""

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()