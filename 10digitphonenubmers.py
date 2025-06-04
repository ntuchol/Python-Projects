import re

def extract_phone_numbers(text):
  """Extracts all 10-digit phone numbers from a string.

  Args:
    text: The string to search for phone numbers.

  Returns:
    A list of all 10-digit phone numbers found in the string.
  """
  phone_numbers = re.findall(r'\b\d{10}\b', text)
  return phone_numbers

# Example usage
text = "My phone number is 1234567890, and my friend's number is 0987654321. There's also 11122233333, which is too long."
phone_numbers = extract_phone_numbers(text)
print(phone_numbers)
# Expected output: ['1234567890', '0987654321']