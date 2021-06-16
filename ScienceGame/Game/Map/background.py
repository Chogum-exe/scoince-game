from PIL import Image
import pygame
import sys
import os
import os.path
import math

PATH = 'images'
TILESIZE = 102
X_TILE_COUNT = 10
Y_TILE_COUNT = 10

class ScrollingBackround():

    def __init__(self, screen_x, screen_y, path=PATH, tilesize=TILESIZE):
        self.path = path
        self.tilesize = tilesize
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.cache = {}

        # Load up all the tiles
        for x in range(X_TILE_COUNT):
            for y in range(Y_TILE_COUNT):
                self.cache[(x,y)] = self._load(x, y)

    def _load(self, x, y):
        img_path = os.path.join(self.path, 'images{}-{}.png'.format(x, y))
        return pygame.image.load(img_path).convert()

    def show(self, screen, x_offset, y_offset):
        for x in range(X_TILE_COUNT):
            for y in range(Y_TILE_COUNT):
                img = self.cache[(x,y)]
                screen.blit(img, (x*self.tilesize-x_offset, y*self.tilesize-y_offset))

                # DEBUG
    def show(self, screen, x_offset, y_offset):
        for x in range(X_TILE_COUNT):
            for y in range(Y_TILE_COUNT):
                img = self.cache[(x,y)]
                screen.blit(img, (x*self.tilesize-x_offset, y*self.tilesize-y_offset))

                # DEBUG
                # pygame.draw.line(
                #     screen, (0, 0, 0),
                #     (x*self.tilesize-x_offset, y*self.tilesize-y_offset),
                #     (x*self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
                # )
                # pygame.draw.line(
                #     screen, (0, 0, 0),
                #     (x*self.tilesize-x_offset, y*self.tilesize-y_offset),
                #     (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize-y_offset),
                # )
                # pygame.draw.line(
                #     screen, (0, 0, 0),
                #     (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize-y_offset),
                #     (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
                # )
                # pygame.draw.line(
                #     screen, (0, 0, 0),
                #     (x*self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
                #     (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
                # )


# ============================================================================

class ScrollingBackround1():
    def __init__(self, path, tilesize):
        self.path = path
        self.tilesize = tilesize
        self.cache = {}
    def _load(self, img, x, y):
         # PilString = image.tostring("raw", strFormat)
         # return pygame.image.fromstring(raw_str, image.size, strFormat)
        self.img = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(self.img, (x, y))
        return self.img
    def _size(self, img):
        self.tileWidth = get_height(img)
        self.tileWidth = get_width(img)
    # def _tile(self, x, y):
    #     return [self.stagePosY % (self.tileHeight * len(self.tiles)) // self.tileHeight, #x1
    #             self.stagePosX % (self.tileWidth * len(self.tiles[0])) // self.tileWidth], # y1
    #             [self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight, #x2
    #             self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth] #y2
    def _quad(self, x, y):
        tiles = _tiles(x,y)
    def _id(self, x, y):
        return 'images/' + str(self.tileWidth) + '-' + str(self.tileHeight)
    def _cache(self, x, y):
        tileX, tileY = _tile(self, x, y)
        if not self.cache:
            self.cache[tileX][tileY] = _load()
    def offset(self, x, y):
        return (0 - self.stagePosX % self.tileWidth,
                0 - self.stagePosY % self.tileHeight)
    def show(self, img, x, y):
        screen.blit(img,(x,y))
    # https://github.com/StevePaget/Pygame_Functions/blob/master/pygame_functions.py
