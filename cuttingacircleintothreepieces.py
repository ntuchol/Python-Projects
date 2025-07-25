import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")  
screen.title("Cutting a Circle")

pen = turtle.Turtle()
pen.speed(0)  
pen.hideturtle() 

radius = 150
center_x = 0
center_y = -radius
pen.penup()
pen.goto(center_x,center_y)
pen.pendown()
pen.circle(radius)

import math
angle1 = 120  
angle2 = 240 
end_x1 = radius * math.cos(math.radians(angle1))
end_y1 = radius * math.sin(math.radians(angle1))
end_x2 = radius * math.cos(math.radians(angle2))
end_y2 = radius * math.sin(math.radians(angle2))


pen.penup()
pen.goto(center_x, center_y+radius)  
pen.pendown()
pen.goto(end_x1, end_y1)

pen.penup()
pen.goto(center_x, center_y+radius)  
pen.pendown()
pen.goto(end_x2, end_y2)

screen.mainloop()
