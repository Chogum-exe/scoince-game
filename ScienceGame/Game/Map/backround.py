import math
import pygame
import sys
import os
sys.path.append(os.getcwd() + '/Game')

import sheetloader
from Player.Python.controller import KeyHandler

class ScrollingBackround():
    def __init__(self, path, tilesize):
        self.path = path
        slef.tilesize = tilesize
    def _load(self, img, x, y):
        self.img = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(self.img, (x, y))
    def  _quadrant(self, x, y, scale):
        return [
            [math.ceil(x, scale), math.floor(y, scale)], [math.ceil(x, scale), math.ceil(y, scale)],
            [math.floor(x, scale), math.floor(y, scale)], [math.floor(x, scale), math.ceil(y, scale)],
        ]
    def show(self, img, x, y):
        screen.blit(img,(x,y))




    def scroll(self, x, y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.stagePosX % self.tileWidth)
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.stagePosY % self.tileHeight)

        col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        screen.blit(self.tiles[row][col], [xOff, yOff])
        screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
        screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])


















import pygame
import time


pygame.init()

window_size = (1000, 562)
screen = pygame.display.set_mode((window_size))
background = pygame.Surface((window_size))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("BG test")

key = KeyHandler(pygame)
bg = ScrollingBackround('Game/Map/backround.jpeg')
# bg.convert_size(window_size[0], window_size[1])


running = True
FPS = 60



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

    pygame.display.flip()
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, window_size[0], window_size[1]))
    bg.show(0,0)
    bg.show(100,500)
    time.sleep(1/FPS)
