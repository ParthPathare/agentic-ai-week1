def decide_next_step(memory: dict) -> str:
    """
    Control flow decides what happens next.
    Runs the agent for two steps before stopping.
    """

    # Force steps to be an integer counter
    if "steps" not in memory or not isinstance(memory["steps"], int):
        memory["steps"] = 0

    if memory["steps"] < 2:
        memory["steps"] += 1
        return "call_llm"

    return "stop"

