import pygame

# pygame 기본 설정
pygame.init()
pygame.display.set_caption("shotting game")

screen_width = 320
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.png")

clock = pygame.time.Clock()
running = True
frame = 0

background_positionX = 0
background_positionY = 0

while running:
    frame += 1
    screen.fill((0,0,0))
    background_positionY -= 1
    if background_positionY < -640:
        background_positionY = (-640)
    screen.blit(background, (background_positionX, background_positionY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    clock.tick(60)
    









#몹:색깔로 구분,색깔마다 다른공격(직선,대각선,곡선,4방향,8방향등)
#맵:일정시간버틴다->랜덤으로 이동 예:파란방,빨간방중 하나로 이동
#방마다 몹 정해져있음
#플래이어:맞으면 죽음 