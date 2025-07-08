from collections import deque

stack = deque()
stack.append(1) # Push
stack.append(2)
stack.append(3)
print(stack.pop()) # Pop, Output: 3
print(stack) # Output: deque([1, 2])