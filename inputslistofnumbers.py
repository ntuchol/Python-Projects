numbers = input("Enter a list of numbers separated by spaces: ")

l = list(map(int, numbers.split()))

print("\nYou entered the list:", l)
print("Sum of the numbers:", sum(l))
print("Maximum number:", max(l))
print("Minimum number:", min(l))
print("Average of the numbers:", sum(l) / len(l) if l else 0)
