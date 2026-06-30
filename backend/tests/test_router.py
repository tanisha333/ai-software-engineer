from agents.tool_router import choose_tool

print(
    choose_tool(
        "Explain config"
    )
)

print(
    choose_tool(
        "Read utils/llm.py"
    )
)

print(
    choose_tool(
        "Find login function"
    )
)