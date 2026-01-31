from llm import llm
from state import AgentState


PROMPT ="Generate a simple HTML page with inline CSS for styling and Javascript for Interactivity and animation for {}" 

def coder(state: AgentState):
    result = llm.invoke(PROMPT.format(state["request"]))
    print("Generated Code:\n", result)
    return {"code": result.content}