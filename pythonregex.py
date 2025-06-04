import re
pattern = r'\bword\b'  # raw string notation is used for regex patterns
text = "This is a word in a sentence."

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")

