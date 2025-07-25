class Ball:
    def __init__(self, x, y, radius, color, x_speed=5, y_speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def bounce(self, width, height):
        if self.x + self.radius > width or self.x - self.radius < 0:
            self.x_speed *= -1
        if self.y + self.radius > height or self.y - self.radius < 0:
            self.y_speed *= -1

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                             self.x + self.radius, self.y + self.radius,
                             fill=self.color)

if __name__ == '__main__':
    import tkinter as tk
    import time

    window = tk.Tk()
    window.title("Bouncing Ball")
    width, height = 600, 400
    canvas = tk.Canvas(window, width=width, height=height, bg="white")
    canvas.pack()

    ball = Ball(100, 100, 20, "red")

    def update():
        ball.move()
        ball.bounce(width, height)
        canvas.delete("all")
        ball.draw(canvas)
        window.after(20, update) 

    update()
    window.mainloop()
