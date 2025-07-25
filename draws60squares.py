import turtle

def draw_squares():
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(0)  

    for i in range(60):
        for _ in range(4):  
            pen.forward(100) 
            pen.right(90)
        pen.right(6)  
    turtle.done()

draw_squares()
