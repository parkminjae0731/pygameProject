import pygame as pg

pg.init()
screen = pg.display.set_mode((300,168))

background_img = pg.image.load("background2.png")
character_img = pg.image.load("character.png")
background_img = pg.transform.scale(background_img, (300,168))
character_img = pg.transform.scale(character_img, (100,100))

running = True

character_img_pos = character_img.get_rect()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                character_img_pos.x -= 5
                
            elif event.key == pg.K_RIGHT:
                character_img_pos.x += 5     
            elif event.key == pg.K_UP:
                character_img_pos.y -= 5
            elif event.key == pg.K_DOWN:
                character_img_pos.y += 5

    screen.blit(background_img,background_img.get_rect())
    screen.blit(character_img,character_img_pos)

    pg.display.update()

pg.quit()