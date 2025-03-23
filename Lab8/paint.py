import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]  # Red, Green, Blue, Black

# Setup Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")
clock = pygame.time.Clock()
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Variables
drawing = False
shape = "free"
current_color = BLACK
start_pos = None

# Game Loop
running = True
while running:
    screen.blit(canvas, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if shape == "rectangle":
                pygame.draw.rect(canvas, current_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
            elif shape == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape == "free":
                pygame.draw.circle(canvas, current_color, event.pos, 5)
            elif shape == "eraser":
                pygame.draw.circle(canvas, WHITE, event.pos, 10)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = "rectangle"
            elif event.key == pygame.K_c:
                shape = "circle"
            elif event.key == pygame.K_f:
                shape = "free"
            elif event.key == pygame.K_e:
                shape = "eraser"
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                current_color = COLORS[event.key - pygame.K_1]
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
