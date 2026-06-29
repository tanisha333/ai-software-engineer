import difflib


def generate_diff(
    original: str,
    updated: str,
):

    diff = difflib.unified_diff(

        original.splitlines(),

        updated.splitlines(),

        fromfile="Original",

        tofile="Updated",

        lineterm=""

    )

    return "\n".join(diff)

old = """
print("Hello")
"""

new = """
print("Hello World")
"""

print(
    generate_diff(old, new)
)
