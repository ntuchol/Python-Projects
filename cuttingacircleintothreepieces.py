import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")  # Optional background color
screen.title("Cutting a Circle")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.hideturtle() # Hide the arrow

# Define circle properties
radius = 150
center_x = 0
center_y = -radius
pen.penup()
pen.goto(center_x,center_y)
pen.pendown()
# Draw the circle
pen.circle(radius)

# Calculate points for cuts
import math
angle1 = 120  # Degrees for 1st cut
angle2 = 240 # Degrees for 2nd cut
end_x1 = radius * math.cos(math.radians(angle1))
end_y1 = radius * math.sin(math.radians(angle1))
end_x2 = radius * math.cos(math.radians(angle2))
end_y2 = radius * math.sin(math.radians(angle2))


# Draw the cut lines
pen.penup()
pen.goto(center_x, center_y+radius)  # Start at top of circle
pen.pendown()
pen.goto(end_x1, end_y1)

pen.penup()
pen.goto(center_x, center_y+radius)  # Start at top of circle
pen.pendown()
pen.goto(end_x2, end_y2)


# Keep window open until closed manually
screen.mainloop()