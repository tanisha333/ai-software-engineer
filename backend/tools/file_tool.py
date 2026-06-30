from pathlib import Path
from langchain_core.tools import tool


@tool
def read_file(file_path: str) -> str:
    """
    Read the contents of a project file.
    """

    project_root = Path.cwd()

    possible_paths = [
        project_root / file_path,
        project_root / file_path.replace("backend/", "", 1),
    ]

    for path in possible_paths:
        if path.exists() and path.is_file():
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

    return f"Error: File '{file_path}' not found."