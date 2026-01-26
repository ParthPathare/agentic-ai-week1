# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import load_memory, save_memory
# from app.tools import market_explainer_tool


# def run_agent(goal: str):
#     memory = load_memory(goal)

#     print("\n[AGENT] Starting agent")
#     print("[AGENT] Goal:", memory["goal"])

#     while True:
#         print("\n[AGENT] Loop iteration")
#         step = decide_next_step(memory)
#         print("[AGENT] Control decided:", step)

#         if step == "call_llm":
#             response = call_llm(memory["goal"])
#             memory["steps"].append(response)
#             print("[AGENT] LLM Response stored")

#         elif step == "use_tool":
#             result = market_explainer_tool(memory["steps"][-1])
#             memory["steps"].append(result)
#             print("[AGENT] Tool executed")

#         elif step == "stop":
#             print("[AGENT] Agent stopping")
#             save_memory(memory)
#             break

from app.control import decide_next_step
from app.llm import call_llm
from app.memory import load_memory, save_memory
from app.tools import market_explainer_tool


def run_agent(goal: str):
    # Load memory specific to the current goal
    memory = load_memory(goal)

    print("\n[AGENT] Starting agent")
    # Always trust the passed goal, not stored memory
    print("[AGENT] Goal:", goal)

    while True:
        print("\n[AGENT] Loop iteration")
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)

        if step == "call_llm":
            # Use the current goal to generate fresh output
            response = call_llm(goal)
            memory["steps"].append(response)

        elif step == "use_tool":
            result = market_explainer_tool(memory["steps"][-1])
            memory["steps"].append(result)

        elif step == "stop":
            # Persist memory under this specific goal
            save_memory(goal, memory)
            break
