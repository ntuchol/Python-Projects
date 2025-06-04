import turtle

def draw_squares():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(0)  # Set the speed to the fastest

    # Draw 60 squares
    for i in range(60):
        for _ in range(4):  # Draw a square
            pen.forward(100)  # Length of each side
            pen.right(90)
        pen.right(6)  # Rotate slightly for the next square

    # Finish
    turtle.done()

# Run the function
draw_squares()
