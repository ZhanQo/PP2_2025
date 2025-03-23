import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Setup Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake Class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check collision with walls
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            return False
        
        # Check collision with itself
        if new_head in self.body:
            return False
        
        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
        
        return True

    def grow(self):
        self.growing = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

# Food Class
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)
    
    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
                   random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
            if pos not in snake_body:
                return pos
    
    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, GRID_SIZE, GRID_SIZE))

# Initialize Game Objects
snake = Snake()
food = Food(snake.body)
speed = 10
score = 0
level = 1
running = True

# Game Loop
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake.direction != (GRID_SIZE, 0):
        snake.direction = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-GRID_SIZE, 0):
        snake.direction = (GRID_SIZE, 0)
    if keys[pygame.K_UP] and snake.direction != (0, GRID_SIZE):
        snake.direction = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and snake.direction != (0, -GRID_SIZE):
        snake.direction = (0, GRID_SIZE)
    
    # Move Snake
    if not snake.move():
        running = False  # End game on collision
    
    # Check food collision
    if snake.body[0] == food.position:
        snake.grow()
        score += 1
        food = Food(snake.body)
        
        # Level up every 4 points
        if score % 4 == 0:
            level += 1
            speed += 2  # Increase speed
    
    # Draw Elements
    snake.draw()
    food.draw()
    
    # Display Score and Level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
