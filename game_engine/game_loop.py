from game_engine.terminal_interface import type_out, display_title
from game_engine.scene_manager import load_scene, handle_scene
from config import default_settings

def start_game():
    display_title()
    type_out("Booting sequence initiated...", speed=default_settings["text_speed"])
    
    scene = load_scene("intro.json")
    
    while scene:
        scene = handle_scene(scene)
