import tkinter as tk
from tkinter import messagebox, simpledialog
from ui.app_window import AppWindow
from security.encryption import load_or_generate_key, load_encrypted_data
from utils.app_utils import monitor_apps, get_installed_apps
import threading

class AppLocker:
    def __init__(self, master):
        self.master = master
        self.master.title("App Locker")

        self.locked_apps = []
        self.unlock_password = None
        self.password_file = 'data/password.enc'
        self.app_file = 'data/apps.enc'
        self.monitoring = False

        # Encryption key
        self.encryption_key = load_or_generate_key()

        # Load encrypted data
        self.locked_apps, self.unlock_password = load_encrypted_data(
            self.password_file, self.app_file, self.encryption_key
        )

        # GUI Elements
        self.status_label = tk.Label(master, text="Status: Not Monitoring", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        tk.Button(master, text="Start Monitoring", command=self.start_monitoring).pack(pady=5)
        tk.Button(master, text="Stop Monitoring", command=self.stop_monitoring).pack(pady=5)
        tk.Button(master, text="Set Password", command=self.set_password).pack(pady=5)
        tk.Button(master, text="Manage Apps", command=self.manage_apps).pack(pady=5)

    def manage_apps(self):
        AppWindow(self.master, self.locked_apps, self.encryption_key)

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

        pass

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

        pass

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

        pass

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app_locker = AppLocker(root)
    app_locker.run()
