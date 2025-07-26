import re

text = "The quick brown fox jumps over the lazy dog."

match = re.search(r"fox", text)
if match:
    print(f"Found: {match.group()}")

words_with_o = re.findall(r"\b\w*o\w*\b", text)
print(f"Words with 'o': {words_with_o}")

new_text = re.sub(r"quick", "fast", text)
print(f"New text: {new_text}")
