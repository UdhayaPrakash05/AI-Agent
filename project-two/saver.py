import os
from state import AgentState

def saver(state: AgentState):
    folder = "output"

    # 1️⃣ Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # 2️⃣ Correct f-string (NO space, prefix f)
    file_path = f"{folder}/index5.html"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(state["code"])

    print(f"✅ File saved at {file_path}")
    return {}
