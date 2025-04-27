
Natalia Tucholska <ntuchol@bu.edu>
Wed, Apr 16, 1:06 AM (10 days ago)
to me

def sum_series(n):
    if n == 0:
        return 0
    else:
        return n + sum_series(n-1)
def sum_powers_of_two(n):
    """
    Calculate the sum of the first n powers of 2 iteratively.
    For example, if n is 3, it calculates 2^0 + 2^1 + 2^2.
    """
    total_sum = 0
    for i in range(n):
        total_sum += 2**i
    return total_sum

# Example usage:
n = 5
result = sum_powers_of_two(n)
print(f"The sum of the first {n} powers of 2 is: {result}")
a=[i:=1]
k=2
while[print(k),k:=2]:
 while all(k<=a[i-b**k]for b in range(1,1+int(i**(1/k)))):k+=1
 a+=k,;i+=1
def concat_recursive(list_of_strings):
    if not list_of_strings:
        return ""
    else:
        head = list_of_strings[0]
        tail = list_of_strings[1:]
        return head + concat_recursive(tail)

# Example usage
strings = ["hello", " ", "world", "!"]
result = concat_recursive(strings)
print(result)  # Output: hello world!

def recursive_product(data):
    """
    Calculate the product of elements in a list recursively.

    Args:
        data: A list of numbers.

    Returns:
        The product of the elements in the list.
        Returns 1 if the list is empty.
    """
    if not data:
        return 1
    else:
        head, *tail = data
        return head * recursive_product(tail)

# Example usage:
numbers = [1, 2, 3, 4, 5]
product = recursive_product(numbers)
print(f"The product of {numbers} is: {product}") # Output: The product of [1, 2, 3, 4, 5] is: 120

empty_list = []
product_empty = recursive_product(empty_list)
print(f"The product of {empty_list} is: {product_empty}") # Output: The product of [] is: 1


def count_rooms(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    num_rooms = 0

    def flood_fill(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '#':
            return
        grid[row][col] = '#'  # Mark the current cell as visited
        # Recursively explore adjacent cells
        flood_fill(row + 1, col)
        flood_fill(row - 1, col)
        flood_fill(row, col + 1)
        flood_fill(row, col - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                num_rooms += 1
                flood_fill(r, c)

    return num_rooms
# Example usage:
grid = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#", "#"],
    ["#", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#"],
]
num_rooms = count_rooms(grid)
print(f"Number of rooms: {num_rooms}")  # Output: 2
def reverse_search(data, target):
    for i in reversed(range(len(data))):
        if data[i] == target:
            return i
    return -1

# Example Usage
my_list = [10, 20, 30, 40, 50]
target_value = 30

index = reverse_search(my_list, target_value)

if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height_of_binary_tree(root):
    if root is None:
        return 0
    else:
        left_height = height_of_binary_tree(root.left)
        right_height = height_of_binary_tree(root.right)
        return max(left_height, right_height) + 1