import pyautogui
import time

delay = 0.001 / 128
clicks = 2000

time.sleep(5)
for i in range(clicks):
    pyautogui.click()
    time.sleep(delay)

