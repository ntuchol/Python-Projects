import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Mondrian Painting")
turtle.speed(0)  # Set drawing speed to fastest

# Define colors
colors = ["red", "yellow", "blue"]

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Generate and draw rectangles
for _ in range(20):  # Example: draw 20 rectangles
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    width = random.randint(50, 200)
    height = random.randint(50, 150)
    color = random.choice(colors)
    draw_rectangle(x, y, width, height, color)

turtle.done() # Keep the turtle window open until closed manually