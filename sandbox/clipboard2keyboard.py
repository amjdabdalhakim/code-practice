import json
import time
import pyperclip
from pynput import keyboard

CONFIG_PATH = "config.json"

def load_config():
    default_config = {
        "hotkey": "<ctrl>+<shift>+v",
        "typing_delay": 0.02,
        "pre_delay": 0.1,
        "safe_mode": False,
        "fallback_paste": False
    }
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
        return default_config


config = load_config()
HOTKEY = config.get("hotkey", "<ctrl>+<shift>+v")
TYPING_DELAY = config.get("typing_delay", 0.02)
PRE_DELAY = config.get("pre_delay", 0.1)
SAFE_MODE = config.get("safe_mode", False)

is_typing = False

def type_text(text, controller):
    if SAFE_MODE or TYPING_DELAY > 0.05:
        for ch in text:
            controller.type(ch)
            time.sleep(TYPING_DELAY)
    else:
        controller.type(text)

def on_activate_hotkey():
    global is_typing
    if is_typing:
        return
    
    is_typing = True
    try:
        text = pyperclip.paste()
        if not text:
            return

        time.sleep(PRE_DELAY)

        with keyboard.Controller() as controller:
            type_text(text, controller)

    except Exception as e:
        print(e)
    finally:
        is_typing = False

def main():
    try:
        hotkey_obj = keyboard.HotKey(
            keyboard.HotKey.parse(HOTKEY),
            on_activate_hotkey
        )

        with keyboard.Listener(
            on_press=hotkey_obj.press,
            on_release=hotkey_obj.release
        ) as listener:
            listener.join()
            
    except KeyboardInterrupt as ki:
        print(ki)

if __name__ == "__main__":
    main()
