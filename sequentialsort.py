def sequential_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sequential_sort(numbers)
print("Sorted list:", sorted_numbers)
