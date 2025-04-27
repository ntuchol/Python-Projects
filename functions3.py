def karatsuba_multiply(x, y):
    if x < 10 and y < 10:
        return x * y
    sx = str(x)
    sy = str(y)
    m = max(len(sx), len(sy))

    sx = '0' * (m - len(sx)) + sx
    sy = '0' * (m - len(sy)) + sy

    m1 = m // 2  
    m2 = m // 2

    lox = int(sx[m1:])
    hix = int(sx[:m1])
    loy = int(sy[m1:])
    hiy = int(sy[:m1])

    z0 = karatsuba_multiply(lox, loy)
    z1 = karatsuba_multiply(lox + hix, loy + hiy)
    z2 = karatsuba_multiply(hix, hiy)

    return z2 * (10 ** (2 * m1)) + (z1 - z0 - z2) * (10 ** m1) + z0

def linear_search_multiple(arr, target, num_searches):
    results = []
    for _ in range(num_searches):
        index = -1
        for i in range(len(arr)):
            if arr[i] == target:
                index = i
                break
        results.append(index)
    return results

import itertools
 
def string_permutations(input_string):
    perms = itertools.permutations(input_string)
    for perm in perms:
        print(''.join(perm))
 
string_permutations("abc")

def getCombos(chars, k):
    if k == 0:
        return ['']
    if not chars:
        return []
    
    head = chars[0]
    tail = chars[1:]
    
    without_head = getCombos(tail, k)
    with_head = [head + combo for combo in getCombos(tail, k - 1)]
    
    return with_head + without_head

import turtle

def draw_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_box_fractal(turtle, size, depth):
    if depth == 0:
        return
    
    draw_square(turtle, size)

    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            turtle.penup()
            turtle.goto(turtle.xcor() + i * size / 3, turtle.ycor() + j * size / 3)
            turtle.pendown()
            draw_box_fractal(turtle, size / 3, depth - 1)
    
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor())
    turtle.pendown()

screen = turtle.Screen()
screen.setup(width=600, height=600)
turtle = turtle.Turtle()
turtle.speed(0)  # Set speed to fastest
turtle.hideturtle()

size = 200
depth = 3
draw_box_fractal(turtle, size, depth)

screen.mainloop()

import turtle

def peano(level, length):
    if level == 0:
        turtle.forward(length)
    else:
        angle = 90
        peano(level-1, length/3)
        turtle.right(angle)
        peano(level-1, length/3)
        for _ in range(2):
            for _ in range(3):
                turtle.left(angle)
                peano(level-1, length/3)
            angle = -angle
        turtle.left(angle)
        peano(level-1, length/3)

turtle.speed(0)
turtle.penup()
turtle.goto(-220, 220)
turtle.pendown()
turtle.right(45)
peano(2, 600)
turtle.done()