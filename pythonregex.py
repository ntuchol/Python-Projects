import re
pattern = r'\bword\b'  
text = "This is a word in a sentence."

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")

