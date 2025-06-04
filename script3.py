# Iterate over all even numbers between 1 and 100
for number in range(2, 101, 2):  # Start at 2, go up to 100, step by 2
    print(number)

import numpy as np
import matplotlib.pyplot as plt

# Define a non-linear function (e.g., quadratic: f(x) = x^2 + 3x + 2)
def non_linear_function(x):
    return x**2 + 3*x + 2

# Generate 100 random x values within a range (e.g., -10 to 10)
x_values = np.random.uniform(-10, 10, 100)

# Apply the non-linear function to the x values
y_values = non_linear_function(x_values)

# Plot the results to visualize
plt.scatter(x_values, y_values, color='blue', label='Random Points')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Random Values from a Non-Linear Function')
plt.legend()
plt.show()

from scipy.optimize import fsolve

def numerical_root(func, guess):
    return fsolve(func, guess)

# Example usage
root = numerical_root(lambda x: x**3 - 6*x**2 + 11*x - 6, 2)  # Initial guess is 2
print(root)

import math

# Sine of 0 radians
print(math.sin(0)) # Output: 0.0

# Sine of π/2 radians
print(math.sin(math.pi / 2)) # Output: 1.0

# Sine of 30 degrees (converted to radians)
print(math.sin(math.radians(30))) # Output: 0.5

def int_to_roman(num):
    # Define a mapping of integers to Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral

# Input from the user
try:
    number = int(input("Enter an integer: "))
    if 1 <= number <= 3999:
        print(f"The Roman numeral for {number} is {int_to_roman(number)}")
    else:
        print("Please enter a number between 1 and 3999.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
import datetime

def get_weekday():
    # Input three numbers: year, month, and day
    try:
        year = int(input("Enter the year (e.g., 2025): "))
        month = int(input("Enter the month (1-12): "))
        day = int(input("Enter the day (1-31): "))

        # Create a date object
        date = datetime.date(year, month, day)

        # Get the weekday name
        weekday = date.strftime("%A")
        return f"The weekday for {date} is {weekday}."
    except ValueError:
        return "Invalid input. Please ensure you enter a valid date."

# Run the function
print(get_weekday())

class Radio:
    def __init__(self):
        self.is_on = False
        self.volume = 5  # Default volume level
        self.station = 101.1  # Default station frequency

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Radio is now ON.")
        else:
            print("Radio is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Radio is now OFF.")
        else:
            print("Radio is already OFF.")

    def set_station(self, frequency):
        if self.is_on:
            self.station = frequency
            print(f"Tuned to {self.station} FM.")
        else:
            print("Turn the radio ON to set a station.")

    def adjust_volume(self, level):
        if self.is_on:
            if 0 <= level <= 10:
                self.volume = level
                print(f"Volume set to {self.volume}.")
            else:
                print("Volume level must be between 0 and 10.")
        else:
            print("Turn the radio ON to adjust the volume.")

    def status(self):
        if self.is_on:
            print(f"Radio is ON | Station: {self.station} FM | Volume: {self.volume}")
        else:
            print("Radio is OFF.")


# Example usage
radio = Radio()

radio.status()
radio.turn_on()
radio.set_station(99.5)
radio.adjust_volume(7)
radio.status()
radio.turn_off()
radio.status()

def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

text = "abc123def456"
numbers = ''.join([char for char in text if char.isdigit()])
print(numbers)  # Output: 123456

def find_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

# Example usage
my_list = [1, 2, 3, 2, 4, 2]
value_to_find = 2
indices = find_indices(my_list, value_to_find)
print(indices)  # Output: [1, 3, 5]

from itertools import combinations

# Example list
items = ['A', 'B', 'C', 'D']

# Generate all combinations of length 2
comb = combinations(items, 2)

# Convert to a list and print
print(list(comb))
# Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

def greatest_divisor(n):
    # Start checking from n//2 down to 1
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i

# Example usage
number = 100
print(f"The greatest divisor of {number} (other than itself) is {greatest_divisor(number)}.")

import math

# Example
a = 48
b = 18

gcd = math.gcd(a, b)
print(f"The GCD of {a} and {b} is {gcd}")

def is_perfect(number):
  sum_ = sum([x for x in range(1, number) if number % x == 0])
  return sum_ == number
is_perfect(6) # Returns True
is_perfect(10) # Returns False..

from datetime import datetime

# Define two dates
date1 = datetime(2025, 6, 1)
date2 = datetime(2023, 10, 1)

# Calculate the difference
delta = date1 - date2

# Output the result
print(f"Difference: {delta.days} days")

import random

def dispense_random(items):
    if not items:
        return "No items to dispense!"
    return f"Dispensed: {random.choice(items)}"

# Example usage
items = ["Soda", "Chips", "Candy"]
print(dispense_random(items))  # Output: Dispensed: (random item)

import geopandas as gpd
from shapely.geometry import Point, Polygon

# Create sample polygons
polygons = gpd.GeoDataFrame({
    'id': [1, 2],
    'geometry': [
        Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)]),
        Polygon([(3, 3), (5, 3), (5, 5), (3, 5), (3, 3)])
    ]
})

# Create sample points
points = gpd.GeoDataFrame({
    'id': [1, 2, 3, 4],
    'geometry': [
        Point(1, 1), Point(1.5, 1.5), Point(4, 4), Point(6, 6)
    ]
})

# Spatial join to count points per polygon
points_within_polygons = gpd.sjoin(points, polygons, how='inner', predicate='within')
point_counts = points_within_polygons.groupby('id_right').size().reset_index(name='point_count')

# Merge counts back to polygons
polygons = polygons.merge(point_counts, left_on='id', right_on='id_right', how='left').fillna(0)

print(polygons)

from Cities import cities_retriever

cr = cities_retriever.CitiesRetrieverByRect("Sources/dict_all_cities_rect2cities.json")
cities = cr.retrieve_cities(lon_start=-124.71, lon_end=-77.21, lat_start=25.24, lat_end=44.75, num=500) # num is optional, default: 999999
print(cities)
print(len(cities))

cr = cities_retriever.CitiesRetrieverByRegionName("Sources/dict_all_cities_region2cities.json")
cities = cr.retrieve_cities(country="United States", region="Washington", num=500) # region and num are optional
print(cities)
print(len(cities))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5] (order may vary)

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define 3D vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
origin = [0, 0, 0]  # Origin point
ax.quiver(*origin, *vector1, color='r', label='Vector 1')
ax.quiver(*origin, *vector2, color='b', label='Vector 2')

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()