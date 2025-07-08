import pygame
import random

pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Stars")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
star_color = (255, 255, 200)

# Shooting Star Class
class ShootingStar:
    def __init__(self, x, y, speed_x, speed_y, length, color):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.length = length
        self.color = color

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, surface):
        for i in range(self.length):
            alpha = int(255 * (1 - i/self.length))
            color = self.color + (alpha,)
            pygame.draw.circle(surface, color, (int(self.x - i * self.speed_x), int(self.y - i * self.speed_y)), 2)

# Game variables
stars = []
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new shooting stars
    if random.randint(0, 100) < 5:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        speed_x = random.uniform(-2, -1)
        speed_y = random.uniform(-1, 1)
        length = random.randint(10, 30)
        star = ShootingStar(x, y, speed_x, speed_y, length, star_color)
        stars.append(star)

    # Update and draw stars
    screen.fill(black)
    for star in stars:
        star.move()
        star.draw(screen)
    stars = [star for star in stars if 0 < star.x < screen_width and 0 < star.y < screen_height]

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
