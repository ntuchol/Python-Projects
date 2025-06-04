import re

def read_phone_number():
    # Regular expression for U.S. phone number format (XXX-XXX-XXXX)
    phone_pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    
    while True:
        phone_number = input("Enter a U.S. phone number in the format (XXX) XXX-XXXX: ")
        if phone_pattern.match(phone_number):
            print(f"Valid phone number entered: {phone_number}")
            break
        else:
            print("Invalid format. Please try again.")

# Run the program
read_phone_number()