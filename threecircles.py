import turtle

def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def overlapping_circles(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    draw_circle(x1, y1, r1)
    draw_circle(x2, y2, r2)
    draw_circle(x3, y3, r3)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Overlapping Circles")

    turtle.speed(0)
    turtle.hideturtle()

    overlapping_circles(0, 0, 100, 50, 50, 80, -60, 20, 70)

    screen.mainloop()