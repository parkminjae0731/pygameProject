import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("Jumping dino")
MAX_WIDTH = 800
MAX_HEIGHT = 400


def check_collision(
    dino_x,
    dino_y,
    dino_width,
    dino_height,
    tree_x,
    tree_y,
    tree_width,
    tree_height,
    bird_x,
    bird_y,
    bird_width,
    bird_height,
    stone_x,
    stone_y,
    stone_width,
    stone_height,
):
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    tree_rect = pygame.Rect(tree_x, tree_y, tree_width, tree_height)
    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    stone_rect = pygame.Rect(stone_x, stone_y, stone_width, stone_height)
    if dino_rect.colliderect(tree_rect) or dino_rect.colliderect(bird_rect) or dino_rect.colliderect(stone_rect) :
        return True
    return False


def main():
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()
    imgDino1 = pygame.image.load("dino1.png")
    imgDino2 = pygame.image.load("dino2.png")
    dino_height = imgDino1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False
    imgTree = pygame.image.load("tree.png")
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height
    imgbird = pygame.image.load("bird.png")
    bird_height = imgbird.get_size()[1]
    bird_x = MAX_WIDTH
    bird_y = MAX_HEIGHT -259
    score = 0
    imgStone = pygame.image.load("stone.png")
    stone_height = imgStone.get_size()[1]
    stone_x = random.randint(0,800)
    stone_y = 0
    font_text = pygame.font.SysFont(None, 30)
    b = random.randint(7, 70)
    c = 0
    while True:
        key_event = pygame.key.get_pressed()
        a = 11
        if score>c:
            c=score
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif key_event[pygame.K_SPACE]:
                if is_bottom:
                    is_go_up = True
                is_bottom = False
            elif key_event[pygame.K_RIGHT] and dino_x < MAX_WIDTH-50:
                dino_x +=40
            elif key_event[pygame.K_LEFT] and dino_x >0:
                dino_x -=40    
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0
        if is_go_up and dino_y <= jump_top:
            is_go_up = False
        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom

        if score >= 5:
            a += 1
            
        if score >= 10:
            a += 2
            
        if score >= 15:
            a += 1
            
        if score >= 20:
            a += 2
            
        if score >= 25:
            a += 1
        if score >= 30:
            a += 2
            
        if score >= 35:
            a += 1
            
        if score >= 40:
            a += 1
        
        if score >= 45:
            a += 1
            
        if score >= 50:
            a += 2
            
        tree_x -= a
        bird_x -= b
        stone_y += 10
        if tree_x <= 0:
            tree_x = MAX_WIDTH
            score += 1
        screen.blit(imgTree, (tree_x, tree_y))
        if bird_x <= 0 :
            bird_x = MAX_WIDTH 
            b = random.randint(7, 70)
            score += 0.5
        screen.blit(imgbird, (bird_x, bird_y))
        if stone_y >= MAX_HEIGHT :
            stone_x = random.randint(0,800) 
            stone_y = 0
            score += 0.5
        screen.blit(imgStone, (stone_x, stone_y))
        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True
       
        if check_collision(
            dino_x,
            dino_y,
            imgDino1.get_width(),
            imgDino1.get_height(),
            tree_x,
            tree_y,
            imgTree.get_width(),
            imgTree.get_height(),
            bird_x,
            bird_y,
            imgbird.get_width(),
            imgbird.get_height(),
            stone_x,
            stone_y,
            imgStone.get_width(),
            imgStone.get_height(),
            
        ):
          score = 0

        score_text = font_text.render(str(score), True, (0, 0, 0))
        screen.blit(score_text, (MAX_WIDTH / 2 - score_text.get_width() / 2, 10))
        pygame.display.flip()              
        score_text = font_text.render(str(a), True, (255, 0, 0))
        screen.blit(score_text, (MAX_WIDTH / 20 - score_text.get_width() / 2, 10))
        pygame.display.flip()
        score_text = font_text.render(str(c), True, (0, 0, 255))
        screen.blit(score_text, (MAX_WIDTH / 1.2 - score_text.get_width() / 2, 10))
        pygame.display.flip()
        pygame.display.update()
        fps.tick(30)


if __name__ == "__main__":
    main()
