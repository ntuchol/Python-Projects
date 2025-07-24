import re

text = "Contact us at (123) 456-7890 or 987.654.3210. Our office number is +1-111-222-3333."

# A common regex pattern for various phone number formats
# This pattern can be adjusted based on the expected formats
phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

found_numbers = re.findall(phone_pattern, text)

print("Extracted phone numbers (Regex):")
for number in found_numbers:
    print(number)