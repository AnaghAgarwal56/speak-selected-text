import keyboard
import pyperclip
import time
from gtts import gTTS
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

def speak_selected_text():
    try:
        keyboard.press_and_release('ctrl+c')
        time.sleep(0.5)

        text = pyperclip.paste()

        if text.strip() != "":
            print("Speaking:", text)

            filename = "speech.mp4"
            tts = gTTS(text=text, lang='en')
            tts.save(filename)

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            # Wait until audio finishes
            while pygame.mixer.music.get_busy():
                continue

            pygame.mixer.music.unload()
            os.remove(filename)

        else:
            print("No text selected!")

    except Exception as e:
        print("Error:", e)

print("Press Ctrl + Alt + Shift to speak selected text")

keyboard.add_hotkey('ctrl+alt+shift', speak_selected_text)
keyboard.wait()