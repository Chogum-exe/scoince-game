#!/usr/bin/env python3
import pygame
import time
from Map.background import ScrollingBackround

pygame.init()
screen = pygame.display.set_mode((1000, 562))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Science Game :D")

running = True
FPS = 60

ScrollingBackround(0, 0, TILESIZE=50)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.flip()
  screen.fill((0,255,255))
  
  player.run(screen)
  time.sleep(1/FPS)