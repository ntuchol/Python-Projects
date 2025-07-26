import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Triangle with Colored Sides")

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

clock = pygame.time.Clock()

def rotate_point(point, angle, center):
    x, y = point
    cx, cy = center
    radians = math.radians(angle)
    x_new = math.cos(radians) * (x - cx) - math.sin(radians) * (y - cy) + cx
    y_new = math.sin(radians) * (x - cx) + math.cos(radians) * (y - cy) + cy
    return x_new, y_new

def main():
    running = True
    angle = 0  
    center = (WIDTH // 2, HEIGHT // 2)  
    size = 150  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        vertices = [
            (center[0], center[1] - size),  
            (center[0] - size, center[1] + size),  
            (center[0] + size, center[1] + size),  
        ]

        rotated_vertices = [rotate_point(v, angle, center) for v in vertices]

        for i in range(3):
            pygame.draw.line(
                screen,
                COLORS[i],
                rotated_vertices[i],
                rotated_vertices[(i + 1) % 3],
                5,  
            )

        pygame.display.flip()

        angle += 1
        if angle >= 360:
            angle = 0

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
