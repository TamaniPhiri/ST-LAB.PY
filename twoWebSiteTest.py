import pyautogui
import time

# Function to wait for a few seconds
def wait(seconds=2):
    time.sleep(seconds)

# Main script
if __name__ == "__main__":
    # Open Start menu
    pyautogui.hotkey('winleft')

    wait()

    # Type 'Firefox' in the search bar and press Enter to open it
    pyautogui.write('Firefox')
    wait()
    pyautogui.press('enter')

    wait(5)  # Give time for Firefox to open (adjust as needed)

    # Open a new tab in Firefox with CTRL+T
    pyautogui.hotkey('ctrl', 't')
    wait()

    # Search for something on Google in the new tab
    pyautogui.write('Python automation site:google.com')
    pyautogui.press('enter')

    wait(5)  # Give time for the search results to load (adjust as needed)

    # Open another new tab with CTRL+T
    pyautogui.hotkey('ctrl', 't')
    wait()

    # Search for something random on Google in the new tab
    pyautogui.write('Random search site:google.com')
    pyautogui.press('enter')

    wait(5)  # Give time for the search results to load (adjust as needed)
