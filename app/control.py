def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)

    # Stop if done
    if memory["completed"]:
        return "stop"

    # First loop → call LLM
    if len(memory["steps"]) == 0:
        return "call_llm"

    # Second loop → use tool AND mark complete
    if len(memory["steps"]) == 1:
        memory["completed"] = True
        return "use_tool"

    return "stop"
