from cryptography.fernet import Fernet
import json
import os
from tkinter import messagebox


def load_or_generate_key():
    key_file = 'data/secret.key'
    
    # Ensure the 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Check if the key file already exists, if not generate and save it
    if os.path.exists(key_file):
        with open(key_file, 'rb') as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
        return key


def encrypt_data(encryption_key, data):
    fernet = Fernet(encryption_key)
    return fernet.encrypt(data.encode())


def decrypt_data(encryption_key, data):
    fernet = Fernet(encryption_key)
    return fernet.decrypt(data).decode()


def load_encrypted_data(password_file, app_file, encryption_key):
    try:
        with open(password_file, 'rb') as file:
            encrypted_password = file.read()
            unlock_password = decrypt_data(encryption_key, encrypted_password)
    except:
        unlock_password = 'skr'

    try:
        with open(app_file, 'rb') as file:
            encrypted_apps = file.read()
            apps_data = decrypt_data(encryption_key, encrypted_apps)
            locked_apps = json.loads(apps_data)
    except:
        locked_apps = []

    return locked_apps, unlock_password
