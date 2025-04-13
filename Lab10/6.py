import pygame
import time
import random
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="zhankozha"
)
cur = conn.cursor()


username = input("Введите имя пользователя: ")
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if not user:
    print("Пользователь не найден.")
    exit()

user_id = user[0]
cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
level, score = cur.fetchone()

print(f"Привет, {username}! Твой уровень: {level}, счёт: {score}")


pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15 + level * 5 

font = pygame.font.SysFont(None, 35)

def show_score(score):
    value = font.render(f"Счёт: {score}", True, green)
    win.blit(value, [0, 0])

def game_loop():
    global score
    x = width / 2
    y = height / 2
    dx = 0
    dy = 0
    snake = []
    length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True
            break

        x += dx
        y += dy
        win.fill(black)
        pygame.draw.rect(win, red, [foodx, foody, snake_block, snake_block])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == [x, y]:
                game_over = True
                break

        for part in snake:
            pygame.draw.rect(win, white, [part[0], part[1], snake_block, snake_block])

        show_score(score)
        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
            score += 10

        clock.tick(snake_speed)


    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level + 1, user_id))
    conn.commit()

    pygame.quit()
    quit()

game_loop()