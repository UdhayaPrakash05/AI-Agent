from langgraph.graph import StateGraph, START,END
from state import AgentState
from coder import coder
from reviewer import reviewer
from saver import saver



graph = StateGraph(AgentState)
graph.add_node("coder", coder)
graph.add_node("reviewer", reviewer)
graph.add_node("saver", saver)

graph.add_edge(START, "coder")
graph.add_edge("coder", "reviewer")
graph.add_edge("reviewer", "saver")
graph.add_edge("saver", END)

graph.compile().invoke({"request": "A college website Sri sairam engineering college"})