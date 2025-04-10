import json
import os
from config import default_settings


def load_memory():
    path = default_settings["memory_path"]
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {"decisions": [], "traits": {}}


def save_memory(memory):
    path = default_settings["memory_path"]
    with open(path, 'w') as f:
        json.dump(memory, f, indent=4)


def record_decision(memory, decision):
    memory["decisions"].append(decision)
    trait = decision.get("trait")
    if trait:
        memory["traits"][trait] = memory["traits"].get(trait, 0) + 1
    save_memory(memory)


def get_player_trait(memory, trait):
    return memory["traits"].get(trait, 0)
