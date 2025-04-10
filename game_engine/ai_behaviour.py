from game_engine.memory_engine import get_player_trait
from game_engine.terminal_interface import type_out


def ai_greeting(memory):
    trust = get_player_trait(memory, "trust")
    defiance = get_player_trait(memory, "defiance")

    if trust > defiance:
        type_out("\nAI: Welcome back... I missed your trust.")
    elif defiance > trust:
        type_out("\nAI: Ah, the rebel returns. Curious to test me again?")
    else:
        type_out("\nAI: We begin anew. Let's see who you really are this time.")


def ai_reaction(memory, action):
    # Optional: build out more complex AI reactions based on action types
    if action == "betrayal":
        type_out("AI: I see... So that’s who you are.")
    elif action == "cooperate":
        type_out("AI: Cooperation... unexpected, but welcome.")
