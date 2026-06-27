from pathlib import Path

from langchain_core.tools import tool


@tool
def search_code(keyword: str) -> list[str]:
    """
    Search the project for files whose name contains the given keyword.
    """

    project_root = Path.cwd()

    matches = []

    for path in project_root.rglob("*"):

        if path.is_file():

            if keyword.lower() in path.name.lower():

                matches.append(str(path))

    return matches