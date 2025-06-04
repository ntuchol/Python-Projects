import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
pen.speed(0) 
pen.hideturtle()

colors = ["red", "purple", "blue", "green", "yellow", "orange"]

distance = 1
angle = 30
for i in range(200):
    pen.color(colors[i % 6])
    pen.forward(distance)
    pen.right(angle)
    distance += 2

turtle.done()