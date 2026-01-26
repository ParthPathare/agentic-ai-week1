# def decide_next_step(memory: dict) -> str:
#     print("\n[CONTROL] Current memory:", memory)

#     if memory["completed"]:
#         return "stop"

#     if len(memory["steps"]) == 0:
#         return "call_llm"

#     if len(memory["steps"]) == 1:
#         return "use_tool"

#     memory["completed"] = True
#     return "stop"

def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)

    # Stop execution only if this goal is already completed
    if memory["completed"]:
        return "stop"

    # First step: call the LLM
    if len(memory["steps"]) == 0:
        return "call_llm"

    # Second step: use the tool
    if len(memory["steps"]) == 1:
        return "use_tool"

    # Mark goal as completed after all steps
    memory["completed"] = True
    return "stop"
