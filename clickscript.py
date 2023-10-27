import pyautogui
import time

coordinates = [(254, 396), (529, 396), (529, 585), (273, 443), (353, 443)]

delay_between_clicks = 1

num_repetitions = 125

for i in range(num_repetitions):
    for x, y in coordinates:
        pyautogui.moveTo(x, y, duration=0.25)
        pyautogui.click()
        time.sleep(delay_between_clicks)

