def decide_next_step(memory: dict) -> str:
    if memory["completed"]:
        return "stop"

<<<<<<< HEAD
    if len(memory["steps"]) < 2:
=======
    if len(memory["steps"]) == 0:
>>>>>>> main
        return "call_llm"

    memory["completed"] = True
    return "stop"