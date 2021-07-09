#!/usr/bin/env python3
import pygame
# import time

# from Game.Questions.Question import *

# print(GenerateQuestions('Multiple', 'Computer', 1, 0))
# from Game.Player.Python.player import Player

pygame.init()
window = (1000, 562)
screen = pygame.display.set_mode(window)
pygame.Surface(window)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Science Game :D")
programIcon = pygame.image.load('icon.png')
loadingImage = pygame.image.load('loading.png')
pygame.display.set_icon(programIcon)
c = pygame.time.Clock()
running = True
loadingScreen = True
game = False
FPS = 60




while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    c.tick(10)
    screen.blit(loadingImage, (0, 0))
    pygame.display.flip()
    
    while game:
        game = exit()
        c.tick(60)
        # Run it in

  # pygame.display.flip()
  # screen.fill((0,255,255))
  # c.tick(3)
