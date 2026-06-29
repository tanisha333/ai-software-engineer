from pathlib import Path

from langchain_core.tools import tool


@tool
def create_file(file_path: str, content: str = "") -> str:
    """
    Create a new file.
    """

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content,
        encoding="utf-8"
    )

    return f"Created {file_path}"