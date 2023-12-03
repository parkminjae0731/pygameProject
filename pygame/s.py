import pygame

# pygame 기본 설정
pygame.init()
pygame.display.set_caption("shotting game")

screen_width = 320
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.png")
background = pygame.transform.smoothscale(background, (1920, 1080))

posx=screen_width//2
posy=screen_height-100
rad=14
playercolor = (100, 100, 255)
bulletcolor = (100, 100, 255)
hp = 100
speed=5
engage=5
bulletx = posx
bullety = posy

background_positionY = screen_height - 1080
FLAG_DOWN = False
FLAG_UP = False
FLAG_RIGHT = False
FLAG_LEFT = False
shot = False
clock = pygame.time.Clock()
running = True
frame = 0

while running:
    frame += 1
    screen.fill((0,0,0))
    background_positionY += 0.2
    screen.blit(background, (-1100, background_positionY))
    if background_positionY >= 0:
        background_positionY = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                FLAG_DOWN = True
            if event.key == pygame.K_UP:
                FLAG_UP = True
            if event.key == pygame.K_RIGHT:
                FLAG_RIGHT = True
            if event.key == pygame.K_LEFT:
                FLAG_LEFT = True
            if event.key == pygame.K_SPACE:
                shot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                FLAG_DOWN = False
            if event.key == pygame.K_UP:
                FLAG_UP = False
            if event.key == pygame.K_RIGHT:
                FLAG_RIGHT = False
            if event.key == pygame.K_LEFT:
                FLAG_LEFT = False
            if event.key == pygame.K_SPACE:
                shot = False
    

    if FLAG_DOWN == True:
        posy += speed
    if FLAG_UP == True:
        posy -= speed
    if FLAG_RIGHT == True:
        posx += speed
    if FLAG_LEFT == True:
        posx -= speed        
    if shot == True:
        
        pygame.draw.circle(screen, bulletcolor, (posx, posy),30)
    
    if posx >= 306:
        posx=306
    if posx <=14:
        posx=14
    if posy >=626:
        posy=626
    if posy <=14:
        posy =14       
    pygame.draw.circle(screen, playercolor, (posx, posy), rad)
    pygame.display.update()
    clock.tick(60)
    









