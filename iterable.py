numbers = [1, 2, 3, 4, 5]
string_numbers = [str(num) for num in numbers]
result = ', '.join(string_numbers)
print(result)  

my_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))  

square = lambda x: x**2
print(square(4))  

is_even = lambda x: x % 2 == 0
print(is_even(7))  
print(is_even(8))  



    import pickle
    
    class User:
        def __init__(self, user_id, username):
            self.user_id = user_id
            self.username = username
    
    user = User(1, "example_user")
    
    with open("user.pkl", "wb") as file:
        pickle.dump(user, file)
    
    with open("user.pkl", "rb") as file:
        loaded_user = pickle.load(file)
    
    print(loaded_user.username)  
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator)) 
print(next(my_iterator)) 
print(next(my_iterator)) 

