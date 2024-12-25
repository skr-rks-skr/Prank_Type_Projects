import psutil
import os
import time


def kill_app(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == app_name.lower():
            try:
                os.kill(proc.info['pid'], 9)
                print(f"{app_name} was closed.")
            except Exception as e:
                print(f"Error closing {app_name}: {e}")


def monitor_apps(locked_apps, monitoring_flag):
    while monitoring_flag:
        for app in locked_apps:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'].lower() == app.lower():
                    print(f"{app} is running. Closing it.")
                    kill_app(app)
        time.sleep(1)


def get_installed_apps():
    app_list = []
    program_files = [
        os.getenv('ProgramFiles'), 
        os.getenv('ProgramFiles(x86)'), 
        os.path.expanduser('~\\AppData\\Local')
    ]
    system_exclusions = ['ProgramData']

    for directory in program_files:
        if directory and os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                if any(excluded in root for excluded in system_exclusions):
                    continue
                for file in files:
                    if file.endswith('.exe'):
                        app_list.append(file)
    return sorted(list(set(app_list)), key=lambda x: x.lower())
