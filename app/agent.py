from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory

def run_agent(goal: str):
    memory = init_memory(goal)

    print("Agent started")
    print("Goal:", goal)

    while True:
        step = decide_next_step(memory)

        if step == "call_llm":
            response = call_llm(goal)
            memory["steps"].append(response)
            print("LLM Response:", response)

        elif step == "stop":
            print("Agent stopped")
            break