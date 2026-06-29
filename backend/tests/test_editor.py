from agents.code_editor import edit_code

old = """
def add(a,b):
    return a+b
"""

request = "Add type hints."

print(
    edit_code(
        old,
        request
    )
)