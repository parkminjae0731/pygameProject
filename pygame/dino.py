import pygame
import sys

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
):
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    tree_rect = pygame.Rect(tree_x, tree_y, tree_width, tree_height)
    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    if dino_rect.colliderect(tree_rect) or dino_rect.colliderect(bird_rect):
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
    bird_y = MAX_HEIGHT - 261
    score = 0
    font_text = pygame.font.SysFont(None, 30)
    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0
        if is_go_up and dino_y <= jump_top:
            is_go_up = False
        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom
        tree_x -= 14
        bird_x -= 3.54
        if tree_x <= 0:
            tree_x = MAX_WIDTH
            score += 1
        screen.blit(imgTree, (tree_x, tree_y))
        if bird_x <= 0:
            bird_x = MAX_WIDTH
            score += 1
        screen.blit(imgbird, (bird_x, bird_y))

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
        ):
            pygame.quit()
            sys.exit()

        score_text = font_text.render(str(score), True, (0, 0, 0))
        screen.blit(score_text, (MAX_WIDTH / 2 - score_text.get_width() / 2, 10))
        pygame.display.flip()
        pygame.display.update()
        fps.tick(30)


if __name__ == "__main__":
    main()
