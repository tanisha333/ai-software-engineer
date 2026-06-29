from pathlib import Path

from langchain_core.tools import tool


@tool
def write_file(file_path: str, content: str) -> str:
    """
    Write content to an existing file.
    """

    path = Path(file_path)

    if not path.exists():
        return "File does not exist."

    path.write_text(
        content,
        encoding="utf-8"
    )

    return f"Updated {file_path}"