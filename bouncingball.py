import pygame pygame.init() 
width, height = 1000, 600 
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Bouncing Ball Simulation")
red = (255, 0, 0) 
black = (0, 0, 0) 
ball_pos = [100, 100] 
ball_radius = 40 
speed = [1, 1]
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
screen.fill(black) 
ball_pos[0] += speed[0] 
ball_pos[1] += speed[1] 
if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= width: 
    speed[0] = -speed[0] if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= height: 
    speed[1] = -speed[1] pygame.draw.circle(screen, red, ball_pos, ball_radius) 
    pygame.display.flip()

