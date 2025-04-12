import time
import random


def glitch_text(text):
    """Randomly alters characters in a string to create a glitch effect."""
    glitched = ""
    for char in text:
        if random.random() < 0.1:
            glitched += random.choice("#$%&*@!~")
        else:
            glitched += char
    return glitched


def delay(seconds):
    time.sleep(seconds)
