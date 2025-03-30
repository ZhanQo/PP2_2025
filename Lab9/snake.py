import pygame
import random
import time


pygame.init()

# Константы
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # столкновение со стенами
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            return False
        
        #столкновение с собой
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

# Класс еды
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)
        self.weight = random.randint(1, 3)  # Разный вес еды
        self.spawn_time = time.time()  # Время появления еды
    
    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
                   random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
            if pos not in snake_body:
                return pos
    
    def is_expired(self, lifespan=5):
        return time.time() - self.spawn_time > lifespan  # Проверка на истечение времени жизни еды
    
    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, GRID_SIZE, GRID_SIZE))

# Инициализация объектов игры
snake = Snake()
food = Food(snake.body)
speed = 10
score = 0
level = 1
running = True

# Игровой цикл
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake.direction != (GRID_SIZE, 0):
        snake.direction = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-GRID_SIZE, 0):
        snake.direction = (GRID_SIZE, 0)
    if keys[pygame.K_UP] and snake.direction != (0, GRID_SIZE):
        snake.direction = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and snake.direction != (0, -GRID_SIZE):
        snake.direction = (0, GRID_SIZE)
    
    # змейкф
    if not snake.move():
        running = False  # Завершаем игру 
    
    # Проверка столкновения с едой
    if snake.body[0] == food.position:
        for _ in range(food.weight):  #значение веса еды
            snake.grow()
        score += food.weight  # Увеличиваем счет
        food = Food(snake.body)  # новая еда
        
        # Повышение уровня на 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличиваем скорость
    
    # Проверка
    if food.is_expired():
        food = Food(snake.body)  # Перегенерируем еду
    
    # Отрисовка элементов
    snake.draw()
    food.draw()
    
    # счет и уровнь
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
