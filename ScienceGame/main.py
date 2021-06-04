#!/usr/bin/env python3
import pygame
import time
from Game.Player.Python.player import Player

pygame.init()
screen = pygame.display.set_mode((1000, 562), pygame.RESIZABLE)
running = True
FPS = 60

player = Player(100, 100)

while running:
  pygame.display.flip()
  player.run()
  time.sleep(1/FPS)