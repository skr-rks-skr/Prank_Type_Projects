import webbrowser
import time
import pyautogui
import os
import sys
from dotenv import load_dotenv

load_dotenv()
web_link = os.getenv("Web_Link")
time_duration = os.getenv("Time_Duration")
range_of_open = os.getenv("Range_Of_Open")
speed_of_open = os.getenv("Speed_Of_Open")

Range = int(range_of_open)
Speed = int(speed_of_open)

def web_attack():
    fixed_position = (500, 500)
    max_duration = int(time_duration)  # 2 minutes in seconds
    start_time = time.time()

    if web_link:  
        while True:
            for _ in range(Range):
                # Check if the elapsed time has exceeded the maximum duration
                if (time.time() - start_time) >= max_duration:
                    sys.exit()
                
                # Open the web link
                webbrowser.open(web_link)
                
                # Move the cursor to the fixed position
                pyautogui.moveTo(fixed_position)
                
                # Small delay to prevent high CPU usage
                time.sleep(Speed)
    else:
        exit()

# Call the function to start the process
web_attack()

