from pathlib import Path

from langchain_core.tools import tool


@tool
def list_directory(path: str = ".") -> list[str]:
    """
    List all files and folders in a directory.
    """

    directory = Path(path)

    if not directory.exists():
        return ["Directory not found."]

    return [
        item.name
        for item in directory.iterdir()
    ]