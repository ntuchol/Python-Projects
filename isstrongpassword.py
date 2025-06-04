import re

def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    # Check for digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."

    # Check for special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    return True, "Password is strong."

# Example usage
password = "P@ssw0rd123"
is_strong, message = is_strong_password(password)
print(message)