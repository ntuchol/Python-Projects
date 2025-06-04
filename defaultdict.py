from collections import defaultdict

# Example 1: Default value as an integer (0)
int_dict = defaultdict(int)
int_dict['a'] += 1
print(int_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})

# Example 2: Default value as a list
list_dict = defaultdict(list)
list_dict['a'].append(10)
list_dict['b'].append(20)
print(list_dict)  # Output: defaultdict(<class 'list'>, {'a': [10], 'b': [20]})

# Example 3: Default value using a custom function
def default_factory():
    return "default_value"

custom_dict = defaultdict(default_factory)
print(custom_dict['missing_key'])  # Output: default_value
print(custom_dict)  # Output: defaultdict(<function default_factory at ...>, {'missing_key': 'default_value'})