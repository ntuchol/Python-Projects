

import math

def pythagorean_theorem(a, b):
  """
  Calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem.

  Args:
    a: Length of one leg.
    b: Length of the other leg.

  Returns:
    Length of the hypotenuse.
  """
  c_squared = a**2 + b**2
  c = math.sqrt(c_squared)
  return c

# Example usage:
leg_a = 3
leg_b = 4
hypotenuse = pythagorean_theorem(leg_a, leg_b)
print(f"The length of the hypotenuse is: {hypotenuse}") # Output: The length of the hypotenuse is: 5.0


def is_right_triangle(a, b, c):
    """
    Checks if three side lengths form a right-angled triangle.

    Args:
        a: Length of one side.
        b: Length of another side.
        c: Length of the remaining side.

    Returns:
        True if the sides form a right-angled triangle, False otherwise.
    """
    sides = sorted([a, b, c])  # Sort sides to easily identify the potential hypotenuse
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# Example usage:
side1 = 5
side2 = 12
side3 = 13
if is_right_triangle(side1, side2, side3):
    print("The sides form a right-angled triangle.") # Output: The sides form a right-angled triangle.
else:
    print("The sides do not form a right-angled triangle.")