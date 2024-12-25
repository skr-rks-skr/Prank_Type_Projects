
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
