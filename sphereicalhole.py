import math

def sphere_hole_volume(radius):
    """
    Calculate the volume of a spherical hole.
    Formula for the volume of a sphere: V = (4/3) * π * r^3
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

# Example usage
hole_radius = 5  # Replace with the radius of the hole
hole_volume = sphere_hole_volume(hole_radius)
print(f"The volume of the spherical hole with radius {hole_radius} is {hole_volume:.2f} cubic units.")
