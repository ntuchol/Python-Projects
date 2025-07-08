import turtle

def spiral(turtle, length, angle, multiplier, min_length):
    """
    Draws a spiral recursively using the turtle library.

    Args:
        turtle: The turtle object.
        length: The current length of the side to draw.
        angle: The angle to turn after drawing each side.
        multiplier: The amount to multiply the length by for the next side.
        min_length: The minimum length of a side before stopping.
    """
    if length > min_length:
        turtle.forward(length)
        turtle.left(angle)
        spiral(turtle, length * multiplier, angle, multiplier, min_length)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0) # Set speed to fastest
    pen.pensize(2)
    pen.color("black")
    
    initial_length = 200
    angle_increment = 90
    length_multiplier = 0.95
    minimum_length = 5

    spiral(pen, initial_length, angle_increment, length_multiplier, minimum_length)
    window.mainloop()

if __name__ == "__main__":
    main()
