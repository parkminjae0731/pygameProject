import pygame as pg
import random
# 1. 마우스 버튼 눌렀을때 망치그림 바꾸기
# 2. 두더지 제한시간 이상 지나면 들어가게 하기
# 3. 시간 얼마 안남았을 때 텍스트 색깔 바꾸기

pg.init()
screen = pg.display.set_mode((735, 818))

background_img = pg.image.load("background3.png")
mole_img=pg.image.load("mole.png")
mole_img = pg.transform.scale(mole_img, (246,205))
hammer_img = pg.image.load("hammer.png")
hammer_img = pg.transform.scale(hammer_img, (80,80))
hammer2_img = pg.image.load("hammer 2.png")
hammer2_img = pg.transform.scale(hammer2_img, (80,80))
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
mole_creation_times = []
moles = []
pg.mouse.set_visible(False)
while running:
    
    screen.blit(background_img, background_img.get_rect())
    
    #점수와 초를 나타내는 코드
    time_text = font.render(str(pg.time.get_ticks() // 1000)
    + "초", True, (0,0,0), None)
    score_text = font.render(str(score) + "점", True, (0,0,0), None)
     
    if limit_time - pg.time.get_ticks() // 1000 <= 5:
        time_text = font.render(str(pg.time.get_ticks() // 1000)
        + "초", True, (255,0,0), None)
        score_text = font.render(str(score) + "점", True, (255,0,0), None)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # 두더지를 클릭했을때 점수를 올리는 코드
        if event.type == pg.MOUSEBUTTONDOWN:
            hammer_img = hammer2_img
            for mole, creation_time in zip(moles, mole_creation_times):
                if mole.collidepoint(event.pos):
                    moles.remove(mole)
                    mole_creation_times.remove(creation_time)
                    score += 1
                    break
        # task1. 마우스 버튼 눌렀을때 망치그림 바꾸기
        elif event.type == pg.MOUSEBUTTONUP:
            hammer_img = pg.image.load("hammer.png")
            hammer_img = pg.transform.scale(hammer_img, (80,80))
    
    # task2. 두더지 제한시간 이상 지나면 들어가게 하기
    for mole, creation_time in zip(moles, mole_creation_times):
        if pg.time.get_ticks() // 1000 - creation_time >= 3:
            moles.remove(mole)
            mole_creation_times.remove(creation_time)

    if (pg.time.get_ticks() // 1000) % 2 == 0:
        if check_time:
            add_mole = screen.blit(mole_img, random.choice(moles_pos))
            moles.append(add_mole)
            mole_creation_times.append(pg.time.get_ticks() // 1000)
            check_time = False
    else:
        check_time = True
    
    
    for mole in moles:
        screen.blit(mole_img, mole)


    
    # 화면에 시간과 점수를 보여주는 코드
    screen.blit(time_text, (660,55))
    screen.blit(score_text, (55,55))
    
    screen.blit(hammer_img, pg.mouse.get_pos())
    
    # task3. 시간 얼마 안남았을 때 텍스트 색깔 바꾸기
    if pg.time.get_ticks() // 1000 > limit_time:
        if score >= target_score:
            screen.blit(success_img, (220,250))

        if score < target_score:
            screen.blit(fail_img, (220,250))
    
    
    
    
    
    pg.display.update()

pg.quit()
    
    
 
