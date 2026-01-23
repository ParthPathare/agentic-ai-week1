from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import market_explainer_tool
 
def run_agent(goal: str):
    memory = init_memory(goal)
 
    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)
 
    while True:
        print("\n[AGENT] Loop iteration")
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)
 
        if step == "call_llm":
            response = call_llm(goal)
            memory["steps"].append(response)
            print("[AGENT] LLM Response:", response)
 
        elif step == "use_tool":
            result = market_explainer_tool(memory["steps"][-1])
            memory["steps"].append(result)
            print("[AGENT] Tool executed")
 
        elif step == "stop":
            print("[AGENT] Agent stopped cleanly")
            break