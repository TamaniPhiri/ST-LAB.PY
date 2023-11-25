import pyautogui
import time

# Function to wait for a few seconds
def wait(seconds=2):
    time.sleep(seconds)

# Function to open a dialog with a fake loading spinner
def open_fake_loading_dialog():
    pyautogui.alert("Loading...", "Inserting standard checkpoints", button="OK")  # Display a fake loading alert
    wait()

# Function to display a pop-up message
def display_popup_message(message):
    pyautogui.alert(message, "Checkpoint", button="OK")  # Display a pop-up message
    wait()

# Main script
if __name__ == "__main__":
    open_fake_loading_dialog()  # Simulate opening a dialog with a fake loading spinner

    # Simulate some processing time (adjust as needed)
    wait()

    # Display a pop-up message
    display_popup_message("Inserted standard checkpoints successfully.")
