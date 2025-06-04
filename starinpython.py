import turtle

# Set up the screen
ws = turtle.Screen()

# Create a turtle instance
star_turtle = turtle.Turtle()

# Draw a star
for i in range(5):
star_turtle.forward(100)
star_turtle.right(144)

# Finish drawing
turtle.done()
