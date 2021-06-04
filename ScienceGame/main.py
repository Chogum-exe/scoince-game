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
    self.vel = {x:0, y:0}

  def events(listener):
    listener.addEventListner(ord('w'), self.move)
    listener.addEventListner(ord('a'), self.move)
    listener.addEventListner(ord('s'), self.move)
    listener.addEventListner(ord('d'), self.move)
    listener.addEventListner(K_UP, self.move)
    listener.addEventListner(K_LEFT, self.move)
    listener.addEventListner(K_DOWN, self.move)
    listener.addEventListner(K_RIGHT, self.move)

  def move(self, key, pressed):
    print(key)
    if pressed:
      if key == K_UP:
        self.vel.y += 1
      if key == K_LEFT:
        self.vel.x -= 1
      if key == K_DOWN:
        self.vel.y -= 1
      if key == K_RIGHT:
        self.vel.y += 1
        
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
    global running
    for event in events:
      if event.type == QUIT:
        running = False
      value = True if event.type == KEYDOWN else False
      for action in self.actions:
        if action.key == event.key:
          action.callback(action.key, value)

player = Player(100, 100)
listener = EventHandler()

while running:
  listener.loop(pygame.event.get())

  pygame.display.flip()
  player.render()
  time.sleep(1/FPS)