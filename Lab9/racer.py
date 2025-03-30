import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Параметры игры
fps = 60
width = 400
height = 600
speed = 5
score = 0
point = 0
coins_to_speed_up = 5  # Количество монет для увеличения скорости врага

# Цвета
red = (255, 0, 0)
black = (0, 0, 0)

# Шрифты и текст
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# Фон дороги
road = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\3003\4.webp")

# Окно игры
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Гонщик")
t = pygame.time.Clock()

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\3003\1.webp")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score, speed
        self.rect.move_ip(0, speed)
        if self.rect.bottom > height + 80:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# Класс монет
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\3003\3.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
        self.value = random.randint(1, 3)  # Очки, которые дает монета

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > height + 80:
            self.reset_position()

    def reset_position(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, width - 40), 0)
        self.value = random.randint(1, 3)

    def collect(self):
        self.rect.center = (1000, 1000)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\3003\2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < height and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < width and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Создание объектов
P1 = Player()
E1 = Enemy()
M1 = Money()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

cash = pygame.sprite.Group()
cash.add(M1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, M1)

# Таймер увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(road, (0, 0))
    
    # Отображение счета
    scores = font_small.render(f"{score}", True, black)
    screen.blit(scores, (10, 10))
    points = font_small.render(f"Очки{point}", True, black)
    screen.blit(points, (380, 10))
    
    # Обновление спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    # столкновения с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    #столкновения с монетой
    collected_money = pygame.sprite.spritecollide(P1, cash, False)
    for money in collected_money:
        point += money.value  # Увеличиваем очки
        money.collect()
    
        # Увеличение скорости
        if point % coins_to_speed_up == 0:
            speed += 0.5
    
    pygame.display.update()
    t.tick(fps)
