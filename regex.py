import re

text = "The quick brown fox jumps over the lazy dog."

# Find the first occurrence of "fox"
match = re.search(r"fox", text)
if match:
    print(f"Found: {match.group()}")

# Find all words with "o"
words_with_o = re.findall(r"\b\w*o\w*\b", text)
print(f"Words with 'o': {words_with_o}")

# Replace "quick" with "fast"
new_text = re.sub(r"quick", "fast", text)
print(f"New text: {new_text}")