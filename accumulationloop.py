numbers = [1, 2, 3, 4, 5]
total = 0  
for number in numbers:
    total += number  
print(total)  

numbers = [1, 2, 3, 4, 5]
product = 1  
for number in numbers:
    product *= number  
print(product)  

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []  
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)  
print(even_numbers)  

words = ["Hello", " ", "World", "!"]
sentence = ""  
for word in words:
    sentence += word  
print(sentence)  
