import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple FPS Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player settings
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50
player_speed = 5

# Bullet settings
bullets = []
bullet_speed = -7
bullet_size = 10

# Target settings
targets = []
target_size = 50
target_spawn_time = 2000  # Spawn every 2 seconds
last_spawn_time = pygame.time.get_ticks()

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Function to draw text
def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_SPACE]:
        # Fire a bullet
        bullets.append([player_pos[0] + player_size // 2, player_pos[1]])

    # Update bullets
    for bullet in bullets[:]:
        bullet[1] += bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn targets
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > target_spawn_time:
        target_x = random.randint(0, WIDTH - target_size)
        targets.append([target_x, 0])
        last_spawn_time = current_time

    # Update targets
    for target in targets[:]:
        target[1] += 2
        if target[1] > HEIGHT:
            targets.remove(target)

    # Check for collisions
    for bullet in bullets[:]:
        for target in targets[:]:
            if (
                target[0] < bullet[0] < target[0] + target_size
                and target[1] < bullet[1] < target[1] + target_size
            ):
                bullets.remove(bullet)
                targets.remove(target)
                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, GREEN, (*player_pos, player_size, player_size))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, bullet, bullet_size)

    # Draw targets
    for target in targets:
        pygame.draw.rect(screen, RED, (*target, target_size, target_size))

    # Draw score
    draw_text(f"Score: {score}", 10, 10)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()