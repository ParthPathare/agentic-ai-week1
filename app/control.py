def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)
 
    if memory["completed"]:
        return "stop"
 
    # Step 1: Get explanation from LLM
    if len(memory["steps"]) == 0:
        return "call_llm"
 
    # Step 2: Present explanation using tool
    if len(memory["steps"]) == 1:
        return "use_tool"
 
    # Step 3: Stop agent
    memory["completed"] = True
    return "stop"