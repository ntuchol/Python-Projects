import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Mondrian Painting")
turtle.speed(0)  
colors = ["red", "yellow", "blue"]

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

for _ in range(20): 
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    width = random.randint(50, 200)
    height = random.randint(50, 150)
    color = random.choice(colors)
    draw_rectangle(x, y, width, height, color)

turtle.done() 
