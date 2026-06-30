from agents.code_reviewer import review_code

code = """
def add(a,b):
    return a+b
"""

print(
    review_code(code)
)