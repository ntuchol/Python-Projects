import turtle

def tree(branch_len, t, angle):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(angle)
        tree(branch_len - 15, t, angle)
        t.left(angle * 2)
        tree(branch_len - 15, t, angle)
        t.right(angle)
        t.backward(branch_len)

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
tree(100, t, 20)
turtle.done()