# Example 1: Basic string replacement
text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # Output: Hello, Python!

# Replace only the first occurrence
text = "apple apple apple"
new_text = text.replace("apple", "orange", 1)
print(new_text)  # Output: orange apple apple

# Replace a character
text = "banana"
new_text = text.replace("a", "o")
print(new_text)  # Output: bonono

# Replace in a list of strings
fruits = ["apple", "banana", "cherry"]
new_fruits = [fruit.replace("a", "o") for fruit in fruits]
print(new_fruits)  # Output: ['opple', 'bonono', 'cherry']


