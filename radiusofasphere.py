import math

def volume_of_sphere(radius):
volume = (4/3) * math.pi * (radius ** 3)
return volume

radius = float(input("Enter the radius of the sphere: "))

volume = volume_of_sphere(radius)

print(f"The volume of the sphere with radius {radius} is {volume:.2f}")
