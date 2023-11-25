import pyautogui
import time

def show_qtpy_and_type_message(message):
    # Adjust these coordinates based on the position of the QtPy application on your screen
    qtpy_icon_position = (100, 100)
    text_field_position = (200, 200)

    try:
        # Move the mouse to the QtPy icon
        pyautogui.moveTo(qtpy_icon_position[0], qtpy_icon_position[1], duration=1)

        # Perform a click to open the QtPy application
        pyautogui.click()

        # Wait for the application to open (you can adjust the sleep duration based on your system)
        time.sleep(2)

        # Move to the text field and type the message
        pyautogui.click(text_field_position[0], text_field_position[1])
        pyautogui.typewrite(message, interval=0.1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace 'Hello, QtPy!' with the message you want to type
    show_qtpy_and_type_message('Hello, QtPy!')
