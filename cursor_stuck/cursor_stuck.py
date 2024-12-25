import pyautogui
import time

position = (200, 300)

start_time = time.time()

try: 
    while True:
        pyautogui.moveTo(position)

        if time.time() - start_time > 10:
            break

except KeyboardInterrupt:
    print("Error")
