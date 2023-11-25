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

    # Type 'Calculator' in the search bar and press Enter to open it
    pyautogui.write('Calculator')
    wait()
    pyautogui.press('enter')

    wait(2)  # Give time for the calculator to open (adjust as needed)

    # Perform addition operation: 2 + 3
    pyautogui.write('2')
    wait()
    pyautogui.press('+')
    wait()
    pyautogui.write('3')
    wait()
    pyautogui.press('enter')

    # Perform subtraction operation: 5 - 2
    wait()
    pyautogui.write('5')
    wait()
    pyautogui.press('-')
    wait()
    pyautogui.write('2')
    wait()
    pyautogui.press('enter')

    # Perform multiplication operation: 4 * 3
    wait()
    pyautogui.write('4')
    wait()
    pyautogui.press('*')
    wait()
    pyautogui.write('3')
    wait()
    pyautogui.press('enter')

    # Perform division operation: 10 / 2
    wait()
    pyautogui.write('10')
    wait()
    pyautogui.press('/')
    wait()
    pyautogui.write('2')
    wait()
    pyautogui.press('enter')

    # Open an alert with a message
    wait()
    pyautogui.alert("Parameterized Test Cases")
