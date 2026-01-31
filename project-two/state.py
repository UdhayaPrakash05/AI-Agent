from typing import TypedDict
class AgentState(TypedDict):
    request: str
    code: str
    review: str