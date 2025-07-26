text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  

text = "apple apple apple"
new_text = text.replace("apple", "orange", 1)
print(new_text)  

text = "banana"
new_text = text.replace("a", "o")
print(new_text)  

fruits = ["apple", "banana", "cherry"]
new_fruits = [fruit.replace("a", "o") for fruit in fruits]
print(new_fruits) 

