def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        inverted_dict[value] = key
    return inverted_dict

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dictionary(original_dict)
print(inverted_dict)
