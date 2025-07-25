from collections import Counter

def element_frequency(arr):
    
    return Counter(arr)

my_array = [1, 2, 2, 3, 1, 4, 1]
frequencies = element_frequency(my_array)
print(frequencies)
