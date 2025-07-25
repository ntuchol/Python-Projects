import math

def euclidean_distance(point1, point2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))
    return distance

point1 = (1, 2)
point2 = (4, 6)
print(euclidean_distance(point1, point2))
