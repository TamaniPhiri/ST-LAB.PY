import pyautogui
import time

# Function to wait for a few seconds
def wait(seconds=2):
    time.sleep(seconds)

# Function to perform a search in the search bar
def search(query):
    pyautogui.hotkey('winleft')  # Press the Windows key to open the Start menu
    wait()
    pyautogui.write(query)       # Type the search query
    wait()
    pyautogui.press('enter')     # Press Enter to perform the search
    wait()

# Function to open Firefox and navigate to Facebook
def open_firefox_and_facebook():
    search("Firefox")            # Search for Firefox
    wait()
    pyautogui.press('enter')     # Open Firefox from the search results
    wait(5)                       # Give Firefox some time to open (adjust as needed)
    
    # Navigate to Facebook
    pyautogui.write("https://www.facebook.com")
    pyautogui.press('enter')
    wait(5)  # Give time for the Facebook page to load (adjust as needed)

    # Simulate login (replace with your actual credentials)
    pyautogui.write("your_email_or_phone")
    pyautogui.press('tab')
    pyautogui.write("your_password")
    pyautogui.press('enter')
    wait(10)  # Give time for the login process (adjust as needed)

# Main script
if __name__ == "__main__":
    open_firefox_and_facebook()
