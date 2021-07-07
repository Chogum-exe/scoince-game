import os

# class Image:
#     __init__(self, x, y, pygame, path):
#         self.pygame = pygame
#         self.path = os.path.join(self.path)
#         self.img = self.pygame.image.load(self.path).convert()
#         self.x = x
#         self.y = y
#     def size():
#         return self.img.get_size()
#
#     def shift(self, x, y):
#         self.x = x
#         self.y = y
#
#     def show(self, screen):
#         screen.blit(self.img, (self.x, self.y))

#This is a historic moment for all memers, for which we have discovered the ultimate power of LIVE SHARE
#we made this together in live share, so we put this here for memories UwU
import pygame
loadImages = {}
def Show(image, type, frame):
    imgCache = loadImages[(image, frame)]
    if loadImages.get((image, frame)) is None:
        # Possible bug if NPC name ends in a number
        try:
            imgPath = 'images/{}/{}-{}.png'.format(type, image, frame))
            imgLoad = pygame.image.load(imgPath).convert_alpha()
            imgCache['img'] = imgLoad
            imgCache['size'] = imgLoad.get_size()
        except:
            if loadImages.get('error') == None
                imgLoad = pygame.image.load('images/npc/error.png').convert()
                loadImages['error'] = imgLoad
            else:
                imgLoad = loadImages['error']
    else:
        imgLoad = loadImages[(image, frame)]
    return imgLoad
