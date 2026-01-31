from llm import llm
from state import AgentState

PROMPT ="Review the Html, CSS and Javascript code for any errors, improvements, and best practices: \n\n{}"

def reviewer(state: AgentState):
    result = llm.invoke(PROMPT.format(state["code"]))
    print("Code Review:\n", result)
    return {"review": result.content}