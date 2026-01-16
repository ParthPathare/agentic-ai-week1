from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import print_tool
 
def run_agent(goal: str):
    print("\n[AGENT] Starting agent")
    memory = init_memory(goal)
 
    while True:
        print("\n[AGENT] Loop iteration started")
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)
 
        if step == "call_llm":
            print("[AGENT] Calling LLM")
            response = call_llm(goal)
            memory["steps"].append(response)
 
        elif step == "use_tool":
            print("[AGENT] Using tool")
            result = print_tool(memory["steps"][-1])
            memory["steps"].append(result)
 
        elif step == "stop":
            print("[AGENT] STOP → exiting loop")
            break
 
    print("[AGENT] Agent finished")
 
 