def decide_next_step(memory: dict) -> str:
    if memory["completed"]:
        return "stop"

    if len(memory["steps"]) == 2:
        return "call_llm"

    memory["completed"] = True
    return "stop"