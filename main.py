string_with_whitespace = "Hello World"
characters_without_whitespace = [char for char in string_with_whitespace if char != " "]
print(characters_without_whitespace)
# Output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
class Array:
    def __init__(self, arr):
        self.arr = arr

    def getMaxNum(self):
        if not self.arr:
            return None  # Handle empty array case
        max_num = self.arr[0]
        for num in self.arr:
            if num > max_num:
                max_num = num
        return max_num

def deletemaxnum_sort(arr):
    sorted_arr = []
    while arr:
        max_index = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        sorted_arr.append(arr.pop(max_index))
    return sorted_arr
def deletemaxnum_sort(arr):
    sorted_arr = []
    while arr:
        max_index = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        sorted_arr.append(arr.pop(max_index))
    return sorted_arr

# Example usage
def deletemaxnum_sort(arr):
    sorted_arr = []
    while arr:
        max_index = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        sorted_arr.append(arr.pop(max_index))
    return sorted_arr

def deletemaxnum_sort(arr):
    sorted_arr = []
    while arr:
        max_index = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        sorted_arr.append(arr.pop(max_index))
    return sorted_arr

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_arr = deletemaxnum_sort(arr.copy())
print(f"Sorted array: {sorted_arr}") # Output: Sorted array: [9, 6, 5, 4, 3, 2, 1, 1]

def remove_duplicates(input_list):
    """Removes duplicate elements from a list while preserving order.

    Args:
        input_list: The list to remove duplicates from.

    Returns:
        A new list with duplicates removed.
    """
    seen = set()
    new_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            new_list.append(item)
    return new_list

class OrderedRecordArray:
    def __init__(self, records=None):
        self._data = []
        if records is not None:
            self.extend(records)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def add(self, record):
        self._data.append(record)
        self._data.sort()

    def extend(self, records):
        for record in records:
            self.add(record)
           
    def merge(self, other):
        if not isinstance(other, OrderedRecordArray):
            raise TypeError("Can only merge with another OrderedRecordArray")
        self.extend(other._data)

def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Bubble elements from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Bubble elements from right to left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1
class MyList:
    def __init__(self, data=None):
        self.data = list(data) if data is not None else []

    def append(self, item):
        self.data.append(item)

    def median(self):
        temp_data = sorted(self.data)
        list_length = len(temp_data)
        if list_length == 0:
            return None
        if list_length % 2 == 0:
            mid1 = temp_data[list_length // 2 - 1]
            mid2 = temp_data[list_length // 2]
            return (mid1 + mid2) / 2
        else:
            return temp_data[list_length // 2]

class Array:
    def __init__(self, data):
        self.data = data

    def deduplicate(self):
        """Removes duplicate elements from the array in place."""
        if len(self.data) <= 1:
            return  # Nothing to deduplicate for empty or single-element arrays

        # Create a new array to store the unique elements.
        unique_data = []
        
        # Iterate through the original array.
        seen = set()
        for element in self.data:
            if element not in seen:
                unique_data.append(element)
                seen.add(element)

        # Update the self.data with the unique elements
        self.data = unique_data

def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        # Odd phase
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        # Even phase
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr
def insertion_sort_modified(arr, reverse=False, optimized=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if optimized:
            # Optimized version using binary search to find the correct position
            low = 0
            high = j
            while low <= high:
                mid = (low + high) // 2
                if (arr[mid] < key if reverse else arr[mid] > key):
                    high = mid - 1
                else:
                    low = mid + 1
            
            j = low
        else:
            # Original version with linear search
            while j >= 0 and (arr[j] < key if reverse else arr[j] > key):
                arr[j + 1] = arr[j]
                j -= 1