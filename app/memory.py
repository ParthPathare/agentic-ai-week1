# import json
# import os

# MEMORY_FILE = "agent_memory.json"


# def load_memory(goal: str) -> dict:
#     if os.path.exists(MEMORY_FILE):
#         print("[MEMORY] Loading existing memory from file")
#         with open(MEMORY_FILE, "r") as f:
#             return json.load(f)

#     print("[MEMORY] Initializing new memory")
#     return {
#         "goal": goal,
#         "steps": [],
#         "completed": False
#     }


# def save_memory(memory: dict):
#     with open(MEMORY_FILE, "w") as f:
#         json.dump(memory, f, indent=2)
#     print("[MEMORY] Memory saved to file")

import json
import os

MEMORY_FILE = "agent_memory.json"


def _load_all_memory() -> dict:
    # Load entire memory store (supports multiple goals)
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}


def load_memory(goal: str) -> dict:
    all_memory = _load_all_memory()

    if goal in all_memory:
        # Return memory specific to the requested goal
        return all_memory[goal]

    # Initialize fresh memory when goal is new
    return {
        "steps": [],
        "completed": False
    }


def save_memory(goal: str, memory: dict):
    all_memory = _load_all_memory()

    # Save memory under the goal key instead of overwriting
    all_memory[goal] = memory

    with open(MEMORY_FILE, "w") as f:
        json.dump(all_memory, f, indent=2)
