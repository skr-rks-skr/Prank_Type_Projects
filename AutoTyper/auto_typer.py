from pynput.keyboard import Controller
import time
import pyautogui
import tkinter as tk

# Create a keyboard controller instance
keyboard = Controller()

def auto_type():
    data = entry_data.get()
    delay = float(entry_delay.get())
    counts = int(entry_times.get())
    time.sleep(5)

    start_time = time.time()  # Record the start time

    for i in range(counts):
        keyboard.type(data)
        pyautogui.press("enter")
        time.sleep(delay)

        elapsed_time = time.time() - start_time
        timer_label.config(text=f"Elapsed Time: {elapsed_time:.2f} seconds")
        root.update()

    timer_label.config(text=f"Completed : {elapsed_time:.2f} seconds")
    root.update()

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Auto Typer")
root.geometry("400x350")

tk.Label(root, text="Enter your message:").pack(pady=10)
entry_data = tk.Entry(root, width=40)
entry_data.pack(pady=5)

tk.Label(root, text="Delay time:").pack(pady=10)
entry_delay = tk.Entry(root, width=10)
entry_delay.pack(pady=5)

tk.Label(root, text="Count time:").pack(pady=10)
entry_times = tk.Entry(root, width=10)
entry_times.pack(pady=5)

generate_button = tk.Button(root, text="Start Auto Typing", command=auto_type)
generate_button.pack(pady=20)

timer_label = tk.Label(root, text="")
timer_label.pack()

root.mainloop()
