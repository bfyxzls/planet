import pygame
from pygame.locals import *
from sys import exit

bg_image = '/Users/lind.zhang/github/planet/son/img/bg.png'

# init
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("load image")
# load and convert image
background = pygame.image.load(bg_image).convert()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background, (0, 0))
    pygame.display.update()
