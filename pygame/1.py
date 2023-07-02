import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('pong')
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

bg_color = pygame.Color(50,255,50)
light_grey = (200,200,200)

ball_speed_x = 11 * random.choice((1,-1))
ball_speed_y =11 * random.choice((1,-1))
player_speed = 0
opponent_speed = 10

while True:
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=8
            if event.key == pygame.K_UP:
                 player_speed -=8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=8
            if event.key == pygame.K_UP:
                 player_speed +=8
    
    
    
    ball_animation()
    player_animation()
    opponent_animation()
    screen.fill(bg_color)
    pygame.draw.rect(screen,(0,0,255),player)
    pygame.draw.rect(screen,(255,0,0),opponent)
    pygame.draw.ellipse(screen,(0,255,255),ball)
    pygame.draw.aaline(screen,(255,255,255),(screen_width/2,0),(screen_width/2,screen_height))
    pygame.display.flip()
    clock.tick(60)
    class Raindrop(object):
        def __init__(self):
            self.height = random.randint(4,7)
            self.speed = random.randint(5,10)
            self.x = random.randint(0,SCREEN_WIDTH)
            self.y = -self.height
        def move(self):
            self.y += self.speed
        def draw(self):
            pygame.draw.line(screen,white,(self.x,self.y),(self.x,self.y+self.height),1)
    def main():
        raindrops = []
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            raindrops.append(Raindrop())
            for drop in raindrops:
                drop.move()
                drop.draw()
                if drop.y > SCREEN_HEIGHT:
                    raindrops.remove(drop)
            pygame.display.update()
        
            if __name__=="__main__":
                main()
