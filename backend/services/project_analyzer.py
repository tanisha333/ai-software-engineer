from pathlib import Path
from collections import defaultdict


def get_project_structure(root: str):

    root = Path(root)

    tree = []

    for path in root.rglob("*"):

        if path.is_file():

            tree.append(
                str(path.relative_to(root))
            )

    return tree


def group_by_folder(files):

    folders = defaultdict(list)

    for file in files:

        folder = file.split("/")[0]

        folders[folder].append(file)

    return folders