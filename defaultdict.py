from collections import defaultdict

int_dict = defaultdict(int)
int_dict['a'] += 1
print(int_dict)  

list_dict = defaultdict(list)
list_dict['a'].append(10)
list_dict['b'].append(20)
print(list_dict)  

def default_factory():
    return "default_value"

custom_dict = defaultdict(default_factory)
print(custom_dict['missing_key'])  
print(custom_dict)  
