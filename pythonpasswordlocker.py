from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def add_password(service, password, key):
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{encrypted_password.decode()}\n")

def get_password(service, key):
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            stored_service, encrypted_password = line.strip().split(":")
            if stored_service == service:
                return decrypt_password(encrypted_password.encode(), key)
    return None

def delete_password(service):
    lines = []
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
    with open("passwords.txt", "w") as file:
        for line in lines:
            if not line.startswith(service + ":"):
                file.write(line)

if __name__ == "__main__":
    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()

    add_password("example.com", "my_secure_password", key)
    print("Password for example.com:", get_password("example.com", key))
    delete_password("example.com")
    print("Password for example.com after deletion:", get_password("example.com", key))
