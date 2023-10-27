import pyautogui
import time

# Define a list of coordinates (x, y) to click on
coordinates = [(254, 396), (529, 396), (529, 585), (273, 443), (353, 443)]

# Set the delay between clicks (in seconds)
delay_between_clicks = 1

# Set the number of repetitions
num_repetitions = 125

for i in range(num_repetitions):
    for x, y in coordinates:
        # Move the mouse cursor to the specified point
        pyautogui.moveTo(x, y, duration=0.25)

        # Perform a click at the current cursor position
        pyautogui.click()

        # Wait according to the defined delay between clicks
        time.sleep(delay_between_clicks)

# End the program after the loop is finished
