import turtle

screen = turtle.Screen()
screen.setup(width=600, height=400)
turtle = turtle.Turtle()
turtle.speed(0)
turtle.hideturtle()

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

flag_width = 200
flag_height = 150
stripe_width = flag_width / 3

draw_rectangle(-flag_width/2, flag_height/2, stripe_width, flag_height, "green")

draw_rectangle(-flag_width/2 + stripe_width, flag_height/2, stripe_width, flag_height, "white")

draw_rectangle(-flag_width/2 + 2 * stripe_width, flag_height/2, stripe_width, flag_height, "red")

screen.mainloop()
