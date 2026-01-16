def decide_next_step(memory: dict) -> str:
    if len(memory["steps"]) < 2:
        return "call_llm"

    return "stop"
