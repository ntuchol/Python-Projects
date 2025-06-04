numbers = [1, 2, 3, 4, 5]
string_numbers = [str(num) for num in numbers]
result = ', '.join(string_numbers)
print(result)  # Output: "1, 2, 3, 4, 5"

my_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

lambda arguments: expression
# Add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Square a number
square = lambda x: x**2
print(square(4))  # Output: 16

# Check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(7))  # Output: False
print(is_even(8))  # Output: True



    import pickle
    
    class User:
        def __init__(self, user_id, username):
            self.user_id = user_id
            self.username = username
    
    user = User(1, "example_user")
    
    # Serialize the object
    with open("user.pkl", "wb") as file:
        pickle.dump(user, file)
    
    # Deserialize the object
    with open("user.pkl", "rb") as file:
        loaded_user = pickle.load(file)
    
    print(loaded_user.username)  # Output: example_user
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator)) # Output: 1
print(next(my_iterator)) # Output: 2
print(next(my_iterator)) # Output: 3

# next(my_iterator) would raise StopIteration because there are no more elements

