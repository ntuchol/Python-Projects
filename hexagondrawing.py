import turtle

def draw_hexagon(turtle, side_length):
    """Draws a hexagon using the turtle module.

    Args:
      turtle: The turtle object to draw with.
      side_length: The length of each side of the hexagon.
    """
    for _ in range(6):
        turtle.forward(side_length)
        turtle.left(60)

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    pen = turtle.Turtle()
    pen.speed(2) # Set the drawing speed
    
    draw_hexagon(pen, 100) # Draw a hexagon with sides of 100 pixels
    
    screen.mainloop() # Keep the window open until it's closed manually
