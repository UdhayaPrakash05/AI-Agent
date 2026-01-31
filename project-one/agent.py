from llm import llm
from langgraph.graph import MessagesState, START, StateGraph

def bot(state: MessagesState):
    current_message = state["messages"]
    response = llm.invoke(current_message)
    return {"messages": [response]}

builder = StateGraph(MessagesState)
builder.add_node("bot", bot)
builder.add_edge(START, "bot")
builder.set_finish_point("bot")
graph = builder.compile()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    for event in graph.stream({"messages": [("user", user_input)]}):
        if "bot" in event:
            event["bot"]["messages"][-1].pretty_print() 