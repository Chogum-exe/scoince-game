from PIL import Image
import pygame
import sys
import os
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
        self.error_img = pygame.image.load(path + '/error.png').convert()
        self.currenttile_x = -1
        self.currenttile_y = -1

    def _load(self, x, y):
        try:
            img_path = os.path.join(self.path, 'images{}-{}.png'.format(x, y))
            return pygame.image.load(img_path).convert()
        except:
            return self.error_img

    # def tileeval(self, x, y):
    #     if abs(int(x / self.tilesize) - self.currenttile_x) > 0:
    #         self.currenttile_x = x / self.tilesize
    #         self.currenttile_y = y / self.tilesize
    #         print('new tile')


    def _sector(self, x_offset, y_offset, screen_x, screen_y):
        left   = math.floor(x_offset / self.tilesize)
        top    = math.floor(y_offset / self.tilesize)
        right  = math.floor((screen_x + x_offset)/ self.tilesize)
        bottom = math.floor((screen_y + y_offset) / self.tilesize)
        return (left, top, right, bottom)

    def _tile(self, x, y, screen_x, screen_y, left, top, right, bottom):
        for x_pos in range(left, right + 1):
            for y_pos in range(top, bottom + 1):
                if self.cache.get((x_pos, y_pos)) is None:
                    self.cache[(x_pos, y_pos)] = self._load(x_pos, y_pos)


    def _draw_box(self, screen, x_offset, y_offset, x, y):
        pygame.draw.line(
            screen, (0, 0, 0),
            (x*self.tilesize-x_offset, y*self.tilesize-y_offset),
            (x*self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
        )
        pygame.draw.line(
            screen, (0, 0, 0),
            (x*self.tilesize-x_offset, y*self.tilesize-y_offset),
            (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize-y_offset),
        )
        pygame.draw.line(
            screen, (0, 0, 0),
            (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize-y_offset),
            (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
        )
        pygame.draw.line(
            screen, (0, 0, 0),
            (x*self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
            (x*self.tilesize+self.tilesize-x_offset, y*self.tilesize+self.tilesize-y_offset),
        )
    def show(self, screen, x_offset, y_offset):
        screen_x, screen_y = screen.get_size()
        # self.tileeval(x_offset, y_offset)
        s = self._sector(x_offset, y_offset, screen_x, screen_y)
        left, top, right, bottom = s
        self._tile(x_offset, y_offset, screen_x, screen_y, left, top, right, bottom)
        
        for x in range(left, right + 1):
            for y in range(top, bottom + 1):
                img = self.cache[(x,y)]
                screen.blit(img, (x*self.tilesize-x_offset, y*self.tilesize-y_offset))
                self._draw_box(screen, x_offset, y_offset, x, y)
