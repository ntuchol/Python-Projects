numbers = [1, 2, 3, 4, 5]
total = 0  # Initialize accumulator to 0 for sum
for number in numbers:
    total += number  # Update accumulator by adding current number
print(total)  # Output: 15

numbers = [1, 2, 3, 4, 5]
product = 1  # Initialize accumulator to 1 for product
for number in numbers:
    product *= number  # Update accumulator by multiplying with current number
print(product)  # Output: 120

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []  # Initialize accumulator to an empty list
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)  # Update accumulator by appending even numbers
print(even_numbers)  # Output: [2, 4, 6]

words = ["Hello", " ", "World", "!"]
sentence = ""  # Initialize accumulator to an empty string
for word in words:
    sentence += word  # Update accumulator by concatenating with current word
print(sentence)  # Output: Hello World!