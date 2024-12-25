import tkinter as tk
import time
import threading
import random 

def create_PopUp():
    if time.time() < end_time:
        root = tk.Tk()
        root.title("Alert")

        screen_width = root.winfo_screenwidth()
        screen_hight = root.winfo_screenheight()

        x = random.randint(0, screen_width - 300)
        y = random.randint(0, screen_hight - 100)

        root.geometry(f"300x100+{x}+{y}")
        tk.Label(root, text = "╰‿╯ ERROR : 404 ╰‿╯").pack(pady=20)
        root.after(int(interval * 1000), limited_time)
        root.mainloop()

def limited_time():
    if time.time() < end_time:
        create_PopUp()

def start_prank():
    time.sleep(1 * 5)
    global interval
    interval = .01
    duration = 50
    global end_time
    end_time = time.time() + duration

    thread = threading.Thread(target=create_PopUp)
    thread.start()

    time.sleep(duration)

if __name__ == "__main__":
    start_prank()


# import tkinter as tk
# import time
# import threading
# import random
# import os
# import sys

# def create_PopUp():
#     if time.time() < end_time:
#         root = tk.Tk()
#         root.title("Alert")

#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()

#         x = random.randint(0, screen_width - 300)
#         y = random.randint(0, screen_height - 100)

#         root.geometry(f"300x100+{x}+{y}")
#         tk.Label(root, text="╰‿╯ ERROR : 404 ╰‿╯").pack(pady=20)
#         root.after(int(interval * 1000), limited_time)
#         root.mainloop()

# def limited_time():
#     if time.time() < end_time:
#         create_PopUp()

# def start_prank():
#     time.sleep(1 * 10)
#     global interval
#     interval = 0.01
#     duration = 100
#     global end_time
#     end_time = time.time() + duration

#     thread = threading.Thread(target=create_PopUp)
#     thread.start()

#     time.sleep(duration)
    
#     # Delete the script file itself after the prank is done
#     delete_self()

# def delete_self():
#     try:
#         # Get the absolute path of the currently running script
#         current_file_path = os.path.abspath(sys.argv[0])
#         print(f"Attempting to delete: {current_file_path}")
        
#         # Check if the file exists
#         if os.path.exists(current_file_path):
#             os.remove(current_file_path)
#             print(f"Deleted {current_file_path} successfully.")
#         else:
#             print(f"File not found: {current_file_path}")
#     except Exception as e:
#         print(f"Error deleting file: {e}")

# if __name__ == "__main__":
#     start_prank()
