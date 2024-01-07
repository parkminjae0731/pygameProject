import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((735, 818))

background_img = pg.image.load("background3.png")
mole_img=pg.image.load("mole.png")
mole_img = pg.transform.scale(mole_img, (246,205))
hammer_img = pg.image.load("hammer.png")
hammer_img = pg.transform.scale(hammer_img, (80,80))
fail_img = pg.image.load("fail.png")
success_img = pg.image.load("success.png")

font = pg.font.SysFont("malgungothic", 30)

# 게임 점수 저장
score = 0 
limit_time = 30
target_score = 15

running = True
check_time = True

moles_pos = [(367,324), (120, 324), (250, 150), (0,150), (480,150), (480,520), (0,520), (250,520)]

moles = []
pg.mouse.set_visible(False)
while running:
    
    screen.blit(background_img, background_img.get_rect())
    
    # (1) 시간 및 점수를 문자열 객체로 변환해 변수에 넣어 주세요. (글자색상 자유, 앤티앨리어싱 True, 배경색 없음)
    time_text = font.render(str(pg.time.get_ticks() // 1000)
    + "초", True, (0,0,0), None)
    score_text = font.render(str(score) + "점", True, (0,0,0), None)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # (2) 화면 내에 마우스가 클릭되면 점수를 1씩 증가시키는 코드를 작성해 주세요. 
        if event.type == pg.MOUSEBUTTONDOWN:
            if mole.collidepoint(event.pos):
                    moles.remove(mole)
                    score += 1
                    break
        
    if (pg.time.get_ticks() // 1000) % 2 == 0:
        if check_time:
            add_mole = screen.blit(mole_img, random.choice(moles_pos))
            moles.append(add_mole)
            check_time = False
    else:
        check_time = True
    
    for mole in moles:
        screen.blit(mole_img, mole)


    
    # (3) 시간과 점수를 화면에 표시하는 코드를 작성해 주세요.
    screen.blit(time_text, (660,55))
    screen.blit(score_text, (55,55))
    
    screen.blit(hammer_img, pg.mouse.get_pos())

    if pg.time.get_ticks() // 1000 > limit_time:
        if score >= target_score:
            screen.blit(success_img, (220,250))

        if score < target_score:
            screen.blit(fail_img, (220,250))
    
    
    
    
    
    pg.display.update()

pg.quit()
