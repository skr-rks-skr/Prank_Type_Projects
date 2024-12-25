import random
import string
import time
import pyautogui
from pynput.keyboard import Controller

keyboard = Controller()

def ran_attack():
    char = string.ascii_letters + string.digits + string.punctuation
    # type = ''.join(random.choices(char))

    delay = .0001
    counts = 100
    start_time = time.time()

    for i in range(counts):
        type = ''.join(random.choices(char, k=1))
        keyboard.type(type)
        pyautogui.press("enter")
        time.sleep(delay)

    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

ran_attack()
