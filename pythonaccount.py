import json
import os
import hashlib

def create_account(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user_data = {
        "username": username,
        "password": hashed_password
    }

    with open(f"{username}.json", "w") as file:
        json.dump(user_data, file)
    print(f"Account created successfully for {username}.")

def login(username, password):
    if not os.path.exists(f"{username}.json"):
        print("Invalid username.")
        return False

    with open(f"{username}.json", "r") as file:
        user_data = json.load(file)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user_data["password"] == hashed_password:
        print("Login successful.")
        return True
    else:
        print("Incorrect password.")
        return False

create_account("user1", "password123")
login("user1", "password123")
login("user1", "wrongpassword")
