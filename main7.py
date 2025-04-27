import networkx as nx
import math

def calculate_distance(coord1, coord2):
    """Calculates the distance between two coordinates using the Haversine formula."""
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def find_route(graph, start_coord, end_coord):
    """Finds the shortest route between two coordinates using Dijkstra's algorithm."""
    start_node = min(graph.nodes, key=lambda node: calculate_distance(start_coord, node))
    end_node = min(graph.nodes, key=lambda node: calculate_distance(end_coord, node))
    try:
        path = nx.shortest_path(graph, source=start_node, target=end_node, weight='distance')
        return path
    except nx.NetworkXNoPath:
        return "No route found."

# Example usage (replace with actual road network data)
graph = nx.Graph()
# Add nodes with coordinates
graph.add_node((40.7128, -74.0060)) # New York
graph.add_node((34.0522, -118.2437)) # Los Angeles
graph.add_node((41.8781, -87.6298)) # Chicago
# Add edges with distances
graph.add_edge((40.7128, -74.0060), (34.0522, -118.2437), distance=3935)
graph.add_edge((40.7128, -74.0060), (41.8781, -87.6298), distance=1145)
graph.add_edge((34.0522, -118.2437), (41.8781, -87.6298), distance=2015)

start_coord = (40.7128, -74.0060)
end_coord = (34.0522, -118.2437)
route = find_route(graph, start_coord, end_coord)
print("Driving route:", route)

def find_largest(num1, num2, num3):
    """
    This function takes three numbers as input and prints the largest among them.
    """
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    print("The largest number is", largest)
# Example usage:
a = 10
b = 14
c = 12
find_largest(a, b, c)

def find_largest(num1, num2, num3):
    """
    This function takes three numbers as input and prints the largest among them.
    """
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    print("The largest number is", largest)
# Example usage:
a = 10
b = 14
c = 12
find_largest(a, b, c)

argest_odd = None
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter integer {i+1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

if largest_odd is not None:
    print("The largest odd number entered is:", largest_odd)
else:
    print("No odd numbers were entered.")
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

sum_of_primes = 0
for num in range(3, 1000):
    if is_prime(num):
        sum_of_primes += num

print(sum_of_primes)

def largest_divisor(n):
    """
    Returns the largest divisor of n that is smaller than n.
    If n is prime, returns 1.
    """
    if n <= 1:
        return None  # or raise an exception, depending on desired behavior
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1 # if n is prime

# Example usage
number = 20
largest_div = largest_divisor(number)
print(f"The largest divisor of {number} is {largest_div}")

number = 13
largest_div = largest_divisor(number)
print(f"The largest divisor of {number} is {largest_div}")

number = int(input("Enter an integer: "))

first_printed_number = number * 2
second_printed_number = number + 5

print(first_printed_number)
print(second_printed_number)

