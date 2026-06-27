from pathlib import Path

from langchain_core.documents import Document

from config.settings import (
    PROJECT_PATH,
    SUPPORTED_EXTENSIONS,
    IGNORE_DIRECTORIES,
)


def load_project():

    documents = []

    for file in PROJECT_PATH.rglob("*"):

        if any(
            folder in file.parts
            for folder in IGNORE_DIRECTORIES
        ):
            continue

        if (
            file.is_file()
            and file.suffix in SUPPORTED_EXTENSIONS
        ):

            try:

                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": str(file)
                        },
                    )
                )

            except Exception:
                pass

    return documents