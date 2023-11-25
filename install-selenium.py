import pyautogui
import time
import subprocess

# Function to wait for a few seconds
def wait(seconds=2):
    time.sleep(seconds)

# Function to open the command prompt (cmd)
def open_cmd():
    pyautogui.hotkey('winleft', 'r')  # Press Win + R to open the Run dialog
    wait()
    pyautogui.write("cmd")  # Type 'cmd' and press Enter to open the command prompt
    wait()
    pyautogui.press('enter')
    wait()

# Function to execute a command in the command prompt
def run_cmd_command(command):
    pyautogui.write(command)
    pyautogui.press('enter')
    wait()

# Function to create a Python file and open it in VSCode
def create_and_open_python_file(filename, content):
    pyautogui.hotkey('winleft')  # Press the Windows key to open the Start menu
    wait()
    pyautogui.write("Visual Studio Code")  # Type 'Visual Studio Code' and press Enter
    wait()
    pyautogui.press('enter')
    wait(5)  # Give VSCode some time to open (adjust as needed)

    # Create a new Python file
    pyautogui.hotkey('ctrl', 'n')
    wait()

    # Write content to the file
    pyautogui.write(content)

    # Save the file
    pyautogui.hotkey('ctrl', 's')
    wait()
    pyautogui.write(filename)
    pyautogui.press('enter')
    wait()

# Main script
if __name__ == "__main__":
    open_cmd()

    # Install Selenium using pip
    run_cmd_command("pip install selenium")

    # Content to write to the Python file
    python_code = 'print("Selenium installed")'

    # Create and open a Python file in VSCode
    create_and_open_python_file("selenium_script.py", python_code)
