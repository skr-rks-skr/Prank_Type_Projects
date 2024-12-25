# import tkinter as tk
# from tkinter import messagebox, simpledialog, Toplevel, Checkbutton, IntVar, Scrollbar, Frame, Canvas
# import psutil
# import os
# import threading
# import time

# class AppLocker:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("App Locker")

#         # Initialize settings
#         self.locked_apps = []
#         self.unlock_password = "skr"  # Default password
#         self.monitoring = False
        
#         # GUI Elements
#         tk.Label(master, text="App Locker", font=("Helvetica", 16)).pack(pady=10)
        
#         self.status_label = tk.Label(master, text="Status: Not Monitoring", font=("Helvetica", 12))
#         self.status_label.pack(pady=5)
        
#         tk.Button(master, text="Start Monitoring", command=self.start_monitoring).pack(pady=5)
#         tk.Button(master, text="Stop Monitoring", command=self.stop_monitoring).pack(pady=5)
#         tk.Button(master, text="Set Password", command=self.set_password).pack(pady=5)
#         tk.Button(master, text="Manage Apps", command=self.manage_apps).pack(pady=5)

#     def kill_app(self, app_name):
#         """
#         Kill the process of the specified app by its name.
#         """
#         for proc in psutil.process_iter(['pid', 'name']):
#             if proc.info['name'].lower() == app_name.lower():
#                 try:
#                     os.kill(proc.info['pid'], 9)  # Force kill the process
#                     print(f"{app_name} was closed.")
#                 except Exception as e:
#                     print(f"Error closing {app_name}: {e}")

#     def monitor_apps(self):
#         """
#         Continuously monitor for any restricted apps and kill them if they are opened.
#         """
#         while self.monitoring:
#             for app in self.locked_apps:
#                 for proc in psutil.process_iter(['pid', 'name']):
#                     if proc.info['name'].lower() == app.lower():
#                         print(f"{app} is trying to run. Killing process...")
#                         self.kill_app(app)
#             time.sleep(1)  # Check every second for faster response

#     def start_monitoring(self):
#         """
#         Start the monitoring thread, requiring password.
#         """
#         if self.check_password():
#             if not self.monitoring:
#                 self.monitoring = True
#                 self.status_label.config(text="Status: Monitoring")
#                 self.monitor_thread = threading.Thread(target=self.monitor_apps)
#                 self.monitor_thread.start()
#             else:
#                 messagebox.showinfo("Info", "Monitoring is already active.")

#     def stop_monitoring(self):
#         """
#         Stop the monitoring thread, requiring password.
#         """
#         if self.check_password():
#             if self.monitoring:
#                 self.monitoring = False
#                 self.status_label.config(text="Status: Not Monitoring")
#                 self.monitor_thread.join()  # Ensure the monitoring thread has finished
#             else:
#                 messagebox.showinfo("Info", "Monitoring is not active.")

#     def check_password(self):
#         """
#         Prompt for the password and verify it. Do not show an error if canceled.
#         """
#         password = simpledialog.askstring("Password Required", "Enter password:", show="*")
#         if password is None:
#             return False  # User clicked cancel
#         if password == self.unlock_password:
#             return True
#         else:
#             messagebox.showerror("Error", "Incorrect password!")
#             return False

#     def set_password(self):
#         """
#         Set or change the password, requiring the current password first.
#         """
#         if self.check_password():  # Ask for the current password before allowing the reset
#             new_password = simpledialog.askstring("Set Password", "Enter new password:", show="*")
#             if new_password:
#                 self.unlock_password = new_password
#                 messagebox.showinfo("Info", "Password updated successfully.")
#     def manage_apps(self):
#         """
#         Display all installed apps with checkboxes to lock/unlock apps, with scroll, select all, search functionality,
#         and an add app feature with suggestions.
#         """
#         if not self.check_password():
#             return

#         # Get the list of all installed apps
#         installed_apps = self.get_installed_apps()

#         # Create a new window
#         manage_window = Toplevel(self.master)
#         manage_window.title("Manage Apps")
#         manage_window.geometry("600x700")

#         # Create a frame for the search box and buttons
#         top_frame = Frame(manage_window)
#         top_frame.pack(fill="x", padx=10, pady=5)

#         # Search Entry to filter apps
#         search_entry = tk.Entry(top_frame)
#         search_entry.pack(fill="x", pady=5)

#         # Create a Listbox for suggestions
#         suggestions_listbox = tk.Listbox(top_frame, height=6, selectmode=tk.SINGLE)
#         suggestions_listbox.pack(fill="x", pady=5)
#         suggestions_listbox.bind('<Double-1>', lambda e: self.add_app_from_suggestion(installed_apps, suggestions_listbox))

#         # Create a frame for the app list and scrollbar
#         frame = Frame(manage_window)
#         frame.pack(fill="both", expand=True, padx=10, pady=10)

#         canvas = Canvas(frame)
#         canvas.pack(side="left", fill="both", expand=True)

#         scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
#         scrollbar.pack(side="right", fill="y")

#         canvas.configure(yscrollcommand=scrollbar.set)
#         canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#         inner_frame = Frame(canvas)
#         canvas.create_window((0, 0), window=inner_frame, anchor="nw")

#         # Variables to hold the check states
#         app_vars = {}
#         checkbutton_dict = {}

#         select_all_state = [False]  # This will toggle between select all and deselect all

#         def toggle_select_all():
#             select_all_state[0] = not select_all_state[0]
#             for var in app_vars.values():
#                 var.set(1 if select_all_state[0] else 0)

#         # Create checkboxes for each app
#         for app in installed_apps:
#             var = IntVar(value=1 if app in self.locked_apps else 0)
#             app_vars[app] = var
#             checkbutton = Checkbutton(inner_frame, text=app, variable=var)
#             checkbutton.pack(anchor='w')
#             checkbutton_dict[app] = checkbutton

#         def filter_apps():
#             search_query = search_entry.get().lower()
#             suggestions_listbox.delete(0, tk.END)  # Clear existing suggestions
#             for app in installed_apps:
#                 if search_query in app.lower():
#                     suggestions_listbox.insert(tk.END, app)
#                     checkbutton_dict[app].pack(anchor='w')
#                 else:
#                     checkbutton_dict[app].pack_forget()

#         def add_app_from_suggestion(apps_list, listbox):
#             selected = listbox.curselection()
#             if selected:
#                 app_name = listbox.get(selected[0])
#                 if app_name not in self.locked_apps:
#                     self.locked_apps.append(app_name)
#                     self.save_apps_to_file()
#                     messagebox.showinfo("Info", f"App '{app_name}' added and locked.")
#                     filter_apps()  # Update checkboxes

#         # Bind the search entry to filter the apps as the user types
#         search_entry.bind("<KeyRelease>", lambda event: filter_apps())

#         # Select/Deselect All button
#         select_button = tk.Button(manage_window, text="Select/Deselect All", command=toggle_select_all)
#         select_button.pack(pady=5)

#         def save_apps():
#             self.locked_apps = [app for app, var in app_vars.items() if var.get() == 1]
#             self.save_apps_to_file()
#             messagebox.showinfo("Info", "App lock list updated.")
#             manage_window.destroy()

#         # Save button
#         save_button = tk.Button(manage_window, text="Save", command=save_apps)
#         save_button.pack(pady=5)


# if __name__ == "__main__":
#     root = tk.Tk()
#     app_locker = AppLocker(root)
#     root.mainloop()



import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Checkbutton, IntVar, Scrollbar, Frame, Canvas
import psutil
import os
import threading
import time
from cryptography.fernet import Fernet
import json

class AppLocker:
    def __init__(self, master):
        self.master = master
        self.master.title("App Locker")

        # Initialize settings
        self.locked_apps = []
        self.unlock_password = None  # Password will be loaded or set later
        self.password_file = 'password.enc'
        self.app_file = 'apps.enc'
        self.monitoring = False

        # Encryption key
        self.encryption_key = self.load_or_generate_key()

        # Load encrypted data
        self.load_encrypted_data()

        # GUI Elements
        tk.Label(master, text="App Locker", font=("Helvetica", 16)).pack(pady=10)
        
        self.status_label = tk.Label(master, text="Status: Not Monitoring", font=("Helvetica", 12))
        self.status_label.pack(pady=5)
        
        tk.Button(master, text="Start Monitoring", command=self.start_monitoring).pack(pady=5)
        tk.Button(master, text="Stop Monitoring", command=self.stop_monitoring).pack(pady=5)
        tk.Button(master, text="Set Password", command=self.set_password).pack(pady=5)
        tk.Button(master, text="Manage Apps", command=self.manage_apps).pack(pady=5)

    def load_or_generate_key(self):
        """
        Load the encryption key from a file or generate a new one.
        """
        key_file = 'secret.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as file:
                file.write(key)
            return key

    def encrypt_data(self, data):
        """
        Encrypt the provided data using the Fernet encryption.
        """
        fernet = Fernet(self.encryption_key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self, data):
        """
        Decrypt the provided data using the Fernet encryption.
        """
        fernet = Fernet(self.encryption_key)
        return fernet.decrypt(data).decode()

    def save_encrypted_data(self, filename, data):
        """
        Save the provided data to a file, encrypted.
        """
        with open(filename, 'wb') as file:
            encrypted_data = self.encrypt_data(data)
            file.write(encrypted_data)

    def load_encrypted_data(self):
        """
        Load encrypted password and apps, if they exist. Set default password 'skr' if no password exists.
        """
        if os.path.exists(self.password_file):
            try:
                with open(self.password_file, 'rb') as file:
                    encrypted_password = file.read()
                    self.unlock_password = self.decrypt_data(encrypted_password)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load password: {e}")
                self.unlock_password = 'skr'
                self.save_encrypted_data(self.password_file, self.unlock_password)
        else:
            # Set default password to 'skr' if no password is found
            self.unlock_password = 'skr'
            self.save_encrypted_data(self.password_file, self.unlock_password)

        if os.path.exists(self.app_file):
            try:
                with open(self.app_file, 'rb') as file:
                    encrypted_apps = file.read()
                    apps_data = self.decrypt_data(encrypted_apps)
                    self.locked_apps = json.loads(apps_data)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load locked apps: {e}")
                self.locked_apps = []
        else:
            self.locked_apps = []

    def save_apps_to_file(self):
        """
        Save the locked apps list in an encrypted file, sorted alphabetically.
        """
        apps_data = json.dumps(sorted(self.locked_apps))
        self.save_encrypted_data(self.app_file, apps_data)

    def set_password(self):
        """
        Set or change the password, requiring the current password first.
        """
        if self.check_password():
            new_password = simpledialog.askstring("Set Password", "Enter new password:", show="*")
            if new_password:
                self.unlock_password = new_password
                self.save_encrypted_data(self.password_file, new_password)
                messagebox.showinfo("Info", "Password updated successfully.")
            else:
                messagebox.showwarning("Warning", "Password not changed. No input provided.")

    def check_password(self):
        """
        Prompt for the password and verify it. Do not show an error if canceled.
        """
        password = simpledialog.askstring("Password Required", "Enter password:", show="*")
        if password is None:
            return False  # User clicked cancel
        if password == self.unlock_password:
            return True
        else:
            messagebox.showerror("Error", "Incorrect password!")
            return False

    def kill_app(self, app_name):
        """
        Kill the process of the specified app by its name.
        """
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == app_name.lower():
                try:
                    os.kill(proc.info['pid'], 9)  # Force kill the process
                    print(f"{app_name} was closed.")
                except Exception as e:
                    print(f"Error closing {app_name}: {e}")

    def monitor_apps(self):
        """
        Continuously monitor for any restricted apps and kill them if they are opened.
        """
        while self.monitoring:
            for app in self.locked_apps:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'].lower() == app.lower():
                        print(f"{app} is trying to run. Killing process...")
                        self.kill_app(app)
            time.sleep(1)  # Check every second for faster response

    def start_monitoring(self):
        """
        Start the monitoring thread, requiring password.
        """
        if self.check_password():
            if not self.monitoring:
                self.monitoring = True
                self.status_label.config(text="Status: Monitoring")
                self.monitor_thread = threading.Thread(target=self.monitor_apps, daemon=True)
                self.monitor_thread.start()
            else:
                messagebox.showinfo("Info", "Monitoring is already active.")

    def stop_monitoring(self):
        """
        Stop the monitoring thread, requiring password.
        """
        if self.check_password():
            if self.monitoring:
                self.monitoring = False
                self.status_label.config(text="Status: Not Monitoring")
                if self.monitor_thread.is_alive():
                    self.monitor_thread.join()
            else:
                messagebox.showinfo("Info", "Monitoring is not active.")

    def get_installed_apps(self):
        """
        Collects all installed apps from common directories (Program Files, AppData, etc.),
        excluding system-related files.
        """
        app_list = []
        
        # Directories to scan for installed applications
        program_files = [
            os.getenv('ProgramFiles'), 
            os.getenv('ProgramFiles(x86)'), 
            os.path.expanduser('~\\AppData\\Local')
        ]
        
        # List of known system directories or apps to exclude
        system_exclusions = ['ProgramData']
        
        # Scan the directories for .exe files
        for directory in program_files:
            if directory and os.path.exists(directory):
                for root, dirs, files in os.walk(directory):
                    # Exclude system-related directories
                    if any(excluded in root for excluded in system_exclusions):
                        continue
                    
                    for file in files:
                        if file.endswith('.exe'):  # Only executable files
                            app_list.append(file)
        
        # Remove duplicates and return sorted list
        return sorted(list(set(app_list)), key=lambda x: x.lower())


    def manage_apps(self):
        """
        Display all installed apps with checkboxes to lock/unlock apps, with scroll, select all, and search functionality.
        """
        if not self.check_password():
            return

        # Get the list of all installed apps
        installed_apps = self.get_installed_apps()

        # Create a new window
        manage_window = Toplevel(self.master)
        manage_window.title("Manage Apps")
        manage_window.geometry("500x600")

        # Create a frame for the search box and buttons
        top_frame = Frame(manage_window)
        top_frame.pack(fill="x", padx=10, pady=5)

        # Search Entry to filter apps
        search_entry = tk.Entry(top_frame)
        search_entry.pack(fill="x", pady=5)

        # Create a frame for the app list and scrollbar
        frame = Frame(manage_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        canvas = Canvas(frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        inner_frame = Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Variables to hold the check states
        app_vars = {}
        checkbutton_dict = {}

        select_all_state = [False]  # This will toggle between select all and deselect all

        def toggle_select_all():
            select_all_state[0] = not select_all_state[0]
            for var in app_vars.values():
                var.set(1 if select_all_state[0] else 0)

        # Create checkboxes for each app
        for app in installed_apps:
            var = IntVar(value=1 if app in self.locked_apps else 0)
            app_vars[app] = var
            checkbutton = Checkbutton(inner_frame, text=app, variable=var)
            checkbutton.pack(anchor='w')
            checkbutton_dict[app] = checkbutton

        def filter_apps():
            search_query = search_entry.get().lower()
            for app, var in app_vars.items():
                if search_query in app.lower():
                    checkbutton_dict[app].pack(anchor='w')
                else:
                    checkbutton_dict[app].pack_forget()

        # Bind the search entry to filter the apps as the user types
        search_entry.bind("<KeyRelease>", lambda event: filter_apps())

        # Select/Deselect All button
        select_button = tk.Button(manage_window, text="Select/Deselect All", command=toggle_select_all)
        select_button.pack(pady=5)

        def save_apps():
            self.locked_apps = [app for app, var in app_vars.items() if var.get() == 1]
            self.save_apps_to_file()
            messagebox.showinfo("Info", "App lock list updated.")
            manage_window.destroy()

        # Save button
        save_button = tk.Button(manage_window, text="Save", command=save_apps)
        save_button.pack(pady=5)

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app_locker = AppLocker(root)
    app_locker.run()