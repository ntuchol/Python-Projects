import math

def pythagorean_theorem(a, b):
  
  c_squared = a**2 + b**2
  c = math.sqrt(c_squared)
  return c

leg_a = 3
leg_b = 4
hypotenuse = pythagorean_theorem(leg_a, leg_b)
print(f"The length of the hypotenuse is: {hypotenuse}") 

def is_right_triangle(a, b, c):
      sides = sorted([a, b, c])  
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

side1 = 5
side2 = 12
side3 = 13
if is_right_triangle(side1, side2, side3):
    print("The sides form a right-angled triangle.") 
else:
    print("The sides do not form a right-angled triangle.")
