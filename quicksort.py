import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def time_quicksort(arr):
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    sizes = [100, 1000, 10000, 100000]
    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        time_taken = time_quicksort(arr)
        print(f"Time taken to sort array of size {size}: {time_taken:.6f} seconds")