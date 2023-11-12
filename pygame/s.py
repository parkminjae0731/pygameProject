import pygame, sys, random
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("shotting game")
screen_width = 540
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
bg_color = pygame.Color(255, 255, 255)
player_speed_x=0
player_speed_y=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed_y += 4
            if event.key == pygame.K_UP:
                player_speed_y -= 4
            if event.key == pygame.K_RIGHT:
                player_speed_x += 4
            if event.key == pygame.K_LEFT:
                player_speed_x -= 4


    screen.fill(bg_color)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()









#몹:색깔로 구분,색깔마다 다른공격(직선,대각선,곡선,4방향,8방향등)
#맵:일정시간버틴다->랜덤으로 이동 예:파란방,빨간방중 하나로 이동
#방마다 몹 정해져있음
#플래이어:맞으면 죽음 