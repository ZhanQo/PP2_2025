import pygame
import math
import time
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")


c = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\miley\clock.png.png")
c = pygame.transform.scale(c, (WIDTH, HEIGHT))  
r_h = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\miley\right.png.png")  
l_h = pygame.image.load(r"C:\Users\Есен\OneDrive\Рабочий стол\miley\left.png.png")  


def b_t_c(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, -angle)  
    rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  
    screen.blit(rotated_image, rect.topleft)  


running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(c, (0, 0))  


    now = datetime.now()
    minutes = now.minute
    seconds = now.second

  
    minute_angle = (minutes % 60) * 6  # 
    second_angle = (seconds % 60) * 6  

    b_t_c(r_h, minute_angle, WIDTH // 2, HEIGHT // 2)  
    b_t_c(l_h, second_angle, WIDTH // 2, HEIGHT // 2) 

    pygame.display.flip()  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1) 

pygame.quit()
