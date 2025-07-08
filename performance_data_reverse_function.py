import timeit
import random
import matplotlib.pyplot as plt

def reverse_list_method(my_list):
    my_list.reverse()
    return my_list

def reverse_slicing_method(my_list):
    return my_list[::-1]

def reverse_reversed_method(my_list):
    return list(reversed(my_list))


def measure_performance(func, list_size, num_iterations):
    list_to_reverse = list(range(list_size))
    time_taken = timeit.timeit(lambda: func(list_to_reverse.copy()), number=num_iterations)
    return time_taken / num_iterations


list_sizes = [10, 100, 1000, 10000, 100000]
num_iterations = 1000
reverse_list_times = []
reverse_slicing_times = []
reverse_reversed_times = []

for size in list_sizes:
    reverse_list_times.append(measure_performance(reverse_list_method, size, num_iterations))
    reverse_slicing_times.append(measure_performance(reverse_slicing_method, size, num_iterations))
    reverse_reversed_times.append(measure_performance(reverse_reversed_method, size, numratons))

plt.plot(list_sizes, reverse_list_times, label="reverse() method")
plt.plot(list_sizes, reverse_slicing_times, label="slicing method")
plt.plot(list_sizes, reverse_reversed_times, label="reversed() method")

plt.xlabel("List Size")
plt.ylabel("Average Time (seconds)")
plt.title("Performance of List Reversal Methods")
plt.legend()
plt.grid(True)
plt.show()