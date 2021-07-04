import os

class Image:
    __init__(self, x, y, pygame, path):
        self.pygame = pygame
        self.path = os.path.join(self.path)
        self.img = self.pygame.image.load(self.path).convert()
        self.x = x
        self.y = y
    def size():
        return self.img.get_size()
        
    def shift(self, x, y):
        self.x = x
        self.y = y
    
    def show(self, screen):
        screen.blit(self.img, (self.x, self.y))

#This is a historic moment for all memers, for which we have discovered the ultimate power of LIVE SHARE
#we made this together in live share, so we put this here for memories UwU