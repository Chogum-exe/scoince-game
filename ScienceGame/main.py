#!/usr/bin/env python3
import pygame
import time
from Game.Player.Python.player import Player

pygame.init()
screen = pygame.display.set_mode((1000, 562))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Science Game :D")

running = True
FPS = 60

player = Player(100, 100, pygame)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.flip()
  player.run(screen)

  #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
  time.sleep(1/FPS)