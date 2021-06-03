#!/usr/bin/env python3
import pygame
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((1000, 562), pygame.RESIZABLE)
running = True
player = Player(100, 100)
listener = EventHandler()
FPS = 60

class Player:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  def events(listener):
    listener.addEventListner(ord('w'), self.move)
  def render(self):
    pygame.draw.circle(screen, (222,63,74), (self.x + 100, self.y + 100), 100, 2)

class Action:
  def __init__(self, keyMatch, callback):
    self.key = keyMatch
    self.callback = callback

class EventHandler:
  def __init__(self):
    self.actions = []
  def addEventListner(self, key, callback):
    self.actions.append(Action(key, callback))
  def loop(self, events):
    for event in events:
      if event.type == QUIT:
        running = False
      value = True if event.type == KEYDOWN else False
      for action in self.actions:
        if action.key == event.key:
          action.callback(action.key, value)
          

while running:
  listener.loop(pygame.events.get())

  pygame.display.flip()
  player.render()
  time.sleep(1/FPS)
