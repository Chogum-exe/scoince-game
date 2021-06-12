import math
import pygame
import sys
import os

class ScrollingBackround():
    def __init__(self, path, tilesize):
        self.path = path
        self.tilesize = tilesize
        self.cache = {}
    def _load(self, img, x, y):
        self.img = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(self.img, (x, y))
    def  _quadrant(self, x, y, scale):
        return [
            [x // scale, y // scale + scale], [x // scale + scale, y // scale + scale],
            [x // scale, y // scale],         [x // scale + scale, y // scale],
        ]
    def cachesave(self, list):
        for y in list:
            for x in list:
                if not self.cache[str(x)]:
                    self.cache[str(x)] = x
    def load(self, x, y, scale):
        list = [[]*2]*2
        # May need an extra parent list
        for y in _quadrant(x, y, scale):
            for x in y:
                if self.cache[str(x)]:
                    list[y][x] = self.cache[str(x)]
                else:
                    return load(x, y, scale)
        return list
    def _offest(self, x, y):
        return [x % self.tilesize, y % self.tilesize]
    def show(self, img, x, y):
        screen.blit(img,(x,y))
        # WIP
        # x, y is player position, scale is tile size


    # def scroll(self, x, y):
    #     self.stagePosX -= x
    #     self.stagePosY -= y
    #     col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
    #     xOff = (0 - self.stagePosX % self.tileWidth)
    #     row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
    #     yOff = (0 - self.stagePosY % self.tileHeight)
    #
    #     col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
    #     row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
    #     screen.blit(self.tiles[row][col], [xOff, yOff])
    #     screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
    #     screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
    #     screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])


import pygame
import time


pygame.init()

window_size = (1000, 562)
screen = pygame.display.set_mode((window_size))
background = pygame.Surface((window_size))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("BG test")

bg = ScrollingBackround('Game/Map', 5)
# bg.convert_size(window_size[0], window_size[1])


running = True
FPS = 60



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

    pygame.display.flip()
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, window_size[0], window_size[1]))
    time.sleep(1//FPS)
