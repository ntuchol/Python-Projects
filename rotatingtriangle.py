import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Triangle with Colored Sides")

# Colors
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to rotate a point around a center
def rotate_point(point, angle, center):
    x, y = point
    cx, cy = center
    radians = math.radians(angle)
    x_new = math.cos(radians) * (x - cx) - math.sin(radians) * (y - cy) + cx
    y_new = math.sin(radians) * (x - cx) + math.cos(radians) * (y - cy) + cy
    return x_new, y_new

# Main loop
def main():
    running = True
    angle = 0  # Initial rotation angle
    center = (WIDTH // 2, HEIGHT // 2)  # Center of rotation
    size = 150  # Triangle size

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))

        # Define triangle vertices
        vertices = [
            (center[0], center[1] - size),  # Top vertex
            (center[0] - size, center[1] + size),  # Bottom-left vertex
            (center[0] + size, center[1] + size),  # Bottom-right vertex
        ]

        # Rotate vertices
        rotated_vertices = [rotate_point(v, angle, center) for v in vertices]

        # Draw each side of the triangle with a different color
        for i in range(3):
            pygame.draw.line(
                screen,
                COLORS[i],
                rotated_vertices[i],
                rotated_vertices[(i + 1) % 3],
                5,  # Line thickness
            )

        # Update the display
        pygame.display.flip()

        # Increment angle for rotation
        angle += 1
        if angle >= 360:
            angle = 0

        # Limit frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()