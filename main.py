#!/usr/bin/env python3
import pygame
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((1000, 562), pygame.RESIZABLE)
running = True

FPS = 60

class Player:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  def render(self):
    pygame.draw.circle(screen, (222,63,74), (self.x + 100, self.y + 100), 100, 2)

player = Player(0, 0)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
              if event.key == K_UP:
                player.y += 1
              if event.key == K_DOWN:
                player.y -= 1
              if event.key == K_RIGHT:
                player.x += 1
              if event.key == K_LEFT:
                player.x -= 1

    pygame.display.flip()
    pygame.draw.circle(screen, (245, 150, 25), (100 + player.x, 100 + player.y), 100, 10)
    time.sleep(1/FPS)
