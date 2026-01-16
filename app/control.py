def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)
 
    if memory["completed"]:
        print("[CONTROL] completed=True → STOP")
        return "stop"
 
    if len(memory["steps"]) == 0:
        print("[CONTROL] First step → CALL LLM")
        return "call_llm"
 
    if len(memory["steps"]) == 1:
        print("[CONTROL] Second step → USE TOOL")
        return "use_tool"
 
    print("[CONTROL] All steps done → STOP")
    memory["completed"] = True
    return "stop"