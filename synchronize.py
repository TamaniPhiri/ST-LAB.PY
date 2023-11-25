import pyautogui
import time

# Function to wait for a few seconds
def wait(seconds=2):
    time.sleep(seconds)

# Function to open File Explorer and navigate to the Documents folder
def open_file_explorer_and_documents():
    pyautogui.hotkey('winleft', 'e')  # Open File Explorer
    wait()
    pyautogui.write("Documents")  # Type 'Documents' to navigate to the Documents folder
    pyautogui.press('enter')
    wait()

# Function to create a new folder and text file in the Documents folder
def synchronize_test_cases():
    # Create a new folder
    pyautogui.hotkey('ctrl', 'shift', 'n')  # Create a new folder shortcut
    wait()
    pyautogui.write("TestCasesFolder")  # Type the folder name
    pyautogui.press('enter')
    wait()

    # Create a text file named testcomplete.txt inside the folder
    pyautogui.hotkey('ctrl', 'n')  # Create a new file shortcut
    wait()
    pyautogui.write("testcomplete.txt")  # Type the file name
    pyautogui.press('enter')
    wait()

    # Write content to the text file
    text_content = "Sync complete!"
    pyautogui.write(text_content)

    # Display a confirmation message
    pyautogui.alert("Sync complete!")

# Main script
if __name__ == "__main__":
    open_file_explorer_and_documents()
    synchronize_test_cases()
