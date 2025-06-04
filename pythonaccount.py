import json
import os
import hashlib

def create_account(username, password):
    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Store user data
    user_data = {
        "username": username,
        "password": hashed_password
    }

    # Save user data to a file (e.g., JSON)
    with open(f"{username}.json", "w") as file:
        json.dump(user_data, file)
    print(f"Account created successfully for {username}.")

def login(username, password):
    # Check if the user file exists
    if not os.path.exists(f"{username}.json"):
        print("Invalid username.")
        return False

    # Load user data
    with open(f"{username}.json", "r") as file:
        user_data = json.load(file)

    # Verify password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user_data["password"] == hashed_password:
        print("Login successful.")
        return True
    else:
        print("Incorrect password.")
        return False

# Example usage
create_account("user1", "password123")
login("user1", "password123")
login("user1", "wrongpassword")