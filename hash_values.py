# Hashing immutable objects
print(hash("hello"))  # Hash of a string
print(hash(42))       # Hash of an integer
print(hash((1, 2, 3)))  # Hash of a tuple

# Attempting to hash a mutable object (raises TypeError)
try:
    print(hash([1, 2, 3]))  # Lists are not hashable
except TypeError as e:
    print(e)

# Custom hash function in a class
class MyClass:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

obj = MyClass(10)
print(hash(obj))  # Uses the custom hash function

