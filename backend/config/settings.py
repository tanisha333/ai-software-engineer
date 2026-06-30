from pathlib import Path

PROJECT_PATH = Path.cwd()

CHROMA_DB_PATH = "chroma_db"

EMBEDDING_MODEL = "gemini-embedding-2-preview"

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".md",
    ".json",
}

IGNORE_DIRECTORIES = {
    ".git",
    "venv",
    ".venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
}