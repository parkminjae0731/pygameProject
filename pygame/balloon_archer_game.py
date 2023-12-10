import pygame# Python program to build an archery game
import random

pygame.init()

# Dimensions of the game window
WIDTH, HEIGHT = 600, 500

# Standard Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Paths
balloonPath = "balloon.png"
archerPath = "archer.png"
arrowPath = "arrow.png"

font = pygame.font.Font('freesansbold.ttf', 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Archer")

# To control the frame rate
clock = pygame.time.Clock()
FPS = 30
