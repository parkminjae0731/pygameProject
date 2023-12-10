import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255,0,0)
black=(100,100,255)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pos_x = 320
pos_y = 240

up_speed = 3
up_accel = 0.5

clock = pygame.time.Clock()
while True:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT] and pos_x >10:
        pos_x -= 5
    if key_event[pygame.K_RIGHT] and pos_x < SCREEN_WIDTH-10:
        pos_x += 5
    
    if key_event[pygame.K_UP] and pos_y > 10:
        pos_y -= up_speed
        up_speed += up_accel
    else:
        up_speed = 3

    if key_event[pygame.K_DOWN] and pos_y <SCREEN_HEIGHT-10:
        pos_y +=5

    screen.fill((black))
    pygame.draw.circle(screen,white,(pos_x,pos_y),10)
    pygame.display.update()
    pos_y +=3
    if key_event[pygame.K_SPACE] and pos_y > 10:
        pos_y -= 20
    
    if pos_y >SCREEN_HEIGHT-10:
        pos_y -=3



        