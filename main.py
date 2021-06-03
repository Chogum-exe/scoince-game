#!/usr/bin/env python3
import pygame
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((1000, 562), pygame.RESIZABLE)
running = True
player = Player(100, 100)
listner = EventHandler()
FPS = 60

class Player:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  def render(self):
    pygame.draw.circle(screen, (222,63,74), (self.x + 100, self.y + 100), 100, 2)

class Key_Event:
  def __init__(self, key):
    pass

class EventHandler:
  def __init__(self):
    self.keys = []

  def addEventListner():
    # We will use this function to add events to listen for
    pass
  def loop(self, events):
    for event in events:
      if event.type == QUIT:
        running = False
      value = True if event.type == KEYDOWN else False
      # Put a switch statement and pass value variable to the thing ☜(ﾟヮﾟ☜)
          

while running:
  listner.loop(pygame.events.get())

  pygame.display.flip()
  player.render()
  time.sleep(1/FPS)
