import time
import tkinter as tk
import os


def storage_full():
    gb = int(entry_data.get())
    start_time = time.time()

    chunk_size = 10**6  # 1 MB
    total_size = gb * 10**9  # 10 MB

    # Directory and file path
    directory = "C:\\Program"
    file_path = os.path.join(directory, "program.txt")

    # Create directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)


    with open(file_path, "wb") as f:
        for _ in range(total_size // chunk_size):
            f.write(b"\0" * chunk_size)

    end_time = time.time()

    print(f"Time taken: {end_time - start_time} seconds")


root = tk.Tk()
root.title("Storage full semulator")
root.geometry("250x200")

tk.Label(root, text="Enter ___ GB").pack(pady=10)
entry_data = tk.Entry(root, width=10)
entry_data.pack(pady=5)

generate_button = tk.Button(root, text="Start", command=storage_full)
generate_button.pack(pady=20)

root.mainloop()



# pyinstaller --onefile --windowed --icon=C:\Storage_full\storage.ico storage_full.py
