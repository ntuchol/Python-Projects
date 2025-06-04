# Example usage of range()
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

for i in range(2, 7):
    print(i)  # Output: 2, 3, 4, 5, 6

for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

for i in range(5, -1, -1):
    print(i) # Output: 5, 4, 3, 2, 1, 0
    
# Example of error when using float in range()
try:
    for i in range(0.5, 5.5):
        print(i)
except TypeError as e:
    print(f"Error: {e}") # Output: Error: 'float' object cannot be interpreted as an integer