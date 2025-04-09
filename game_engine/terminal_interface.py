import time
import sys

def type_out(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def glitch_text(text):
    # Add some visual noise to simulate a glitchy AI
    import random
    glitch = ''.join(char if random.random() > 0.1 else '#' for char in text)
    return glitch

def display_title():
    print("\n\033[95m===========================")
    print("     ECHO TERMINAL")
    print("===========================\033[0m\n")

def clear_screen():
    print("\033c", end="")
