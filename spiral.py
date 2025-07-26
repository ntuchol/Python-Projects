import turtle

def spiral(turtle, length, angle, multiplier, min_length):
    
    if length > min_length:
        turtle.forward(length)
        turtle.left(angle)
        spiral(turtle, length * multiplier, angle, multiplier, min_length)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0) 
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
