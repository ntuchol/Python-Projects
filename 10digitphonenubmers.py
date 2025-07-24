import re

def extract_phone_numbers(text):
  phone_numbers = re.findall(r'\b\d{10}\b', text)
  return phone_numbers


text = "My phone number is 1234567890, and my friend's number is 0987654321. There's also 11122233333, which is too long."
phone_numbers = extract_phone_numbers(text)
print(phone_numbers)
