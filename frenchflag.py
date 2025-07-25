import turtle

screen = turtle.Screen()
screen.setup(width=600, height=400)
turtle = turtle.Turtle()
turtle.speed(0)
turtle.penup()

turtle.goto(-300, -200)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

turtle.goto(-100, -200)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

turtle.goto(100, -200)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()
turtle.hideturtle()

screen.mainloop()
