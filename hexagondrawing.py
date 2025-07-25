import turtle

def draw_hexagon(turtle, side_length):
    
    for _ in range(6):
        turtle.forward(side_length)
        turtle.left(60)

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    pen = turtle.Turtle()
    pen.speed(2) 
    
    draw_hexagon(pen, 100) 
    
    screen.mainloop() 
