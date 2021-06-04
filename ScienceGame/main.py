#!/usr/bin/env python3
import pygame
import time
from Game.Player.Python.player import Player
from Game.Player.Python.controller import KeyHandler

pygame.init()
screen = pygame.display.set_mode((1000, 562), pygame.RESIZABLE)
running = True
FPS = 60

player = Player(100, 100, KeyHandler(pygame))

while running:
  pygame.display.flip()
  player.run(screen)
  time.sleep(1/FPS)