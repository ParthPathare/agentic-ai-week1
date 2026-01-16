def decide_next_step(memory: dict) -> str:
    # initialize memory safely
    memory.setdefault("steps", 0)
    memory.setdefault("completed", False)

    if memory["completed"]:
        return "stop"

    if memory["steps"] < 2:
        memory["steps"] += 1
        return "call_llm"

    memory["completed"] = True
    return "stop"
