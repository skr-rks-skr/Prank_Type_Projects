import tkinter as tk
from tkinter import Toplevel, Frame, Canvas, Scrollbar, Checkbutton, IntVar
from utils.app_utils import get_installed_apps


class AppWindow:
    def __init__(self, master, locked_apps, encryption_key):
        self.locked_apps = locked_apps
        self.encryption_key = encryption_key

        # Create a new window
        self.manage_window = Toplevel(master)
        self.manage_window.title("Manage Apps")
        self.manage_window.geometry("500x600")

        # Call method to create UI components
        self.create_ui()

    def create_ui(self):
        top_frame = Frame(self.manage_window)
        top_frame.pack(fill="x", padx=10, pady=5)

        # Search Entry to filter apps
        search_entry = tk.Entry(top_frame)
        search_entry.pack(fill="x", pady=5)

        frame = Frame(self.manage_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        canvas = Canvas(frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        inner_frame = Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        app_vars = {}
        checkbutton_dict = {}

        # Get the list of all installed apps
        installed_apps = get_installed_apps()

        for app in installed_apps:
            var = IntVar(value=1 if app in self.locked_apps else 0)
            app_vars[app] = var
            checkbutton = Checkbutton(inner_frame, text=app, variable=var)
            checkbutton.pack(anchor='w')
            checkbutton_dict[app] = checkbutton

        search_entry.bind("<KeyRelease>", lambda event: self.filter_apps(search_entry, app_vars, checkbutton_dict))

    def filter_apps(self, search_entry, app_vars, checkbutton_dict):
        search_query = search_entry.get().lower()
        for app, var in app_vars.items():
            if search_query in app.lower():
                checkbutton_dict[app].pack(anchor='w')
            else:
                checkbutton_dict[app].pack_forget()
