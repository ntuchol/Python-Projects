# Program to input a list of numbers and perform basic operations

# Input: Prompt the user to enter numbers separated by spaces
numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
l = list(map(int, numbers.split()))

# Output the list and perform basic operations
print("\nYou entered the list:", l)
print("Sum of the numbers:", sum(l))
print("Maximum number:", max(l))
print("Minimum number:", min(l))
print("Average of the numbers:", sum(l) / len(l) if l else 0)