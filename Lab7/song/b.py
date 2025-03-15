import pygame


pygame.init()


WIDTH, HEIGHT = 400, 400
s = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шарик")


rad = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
color = (255, 0, 0)
step = 20

running = True
while running:
    s.fill((255, 255, 255))  
    pygame.draw.circle(s, color, (ball_x, ball_y), rad)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ball_x - rad > 0:
                ball_x -= step
            if event.key == pygame.K_RIGHT and ball_x + rad < WIDTH:
                ball_x += step
            if event.key == pygame.K_UP and ball_y - rad > 0:
                ball_y -= step
            if event.key == pygame.K_DOWN and ball_y + rad < HEIGHT:
                ball_y += step

pygame.quit()
