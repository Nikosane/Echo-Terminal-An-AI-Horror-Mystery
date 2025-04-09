import json
import os
from config import default_settings
from game_engine.terminal_interface import type_out


def load_scene(scene_file):
    path = os.path.join(default_settings["scenes_path"], scene_file)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        type_out("[ERROR] Scene file not found: " + scene_file)
        return None

def handle_scene(scene):
    type_out("\n" + scene.get("description", ""), speed=default_settings["text_speed"])

    if "options" not in scene:
        return None

    for idx, option in enumerate(scene["options"], 1):
        print(f"{idx}. {option['text']}")

    while True:
        try:
            choice = int(input("\n> ")) - 1
            if 0 <= choice < len(scene["options"]):
                return load_scene(scene["options"][choice]["next"])
            else:
                type_out("Invalid choice. Try again.")
        except ValueError:
            type_out("Please enter a valid number.")
