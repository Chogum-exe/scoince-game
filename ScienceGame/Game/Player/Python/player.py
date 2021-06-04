import pygame

class Player:
    def __init__(self, x, y, control):
        self.x = x
        self.y = y
        self.controller = control

    def move(self):
        x_dir, y_dir = self.controller.wasd()
        self.x += x_dir
        self.y += y_dir

    def render(self, screen):
        pygame.draw.circle(screen, (234,63,74), (self.x + 100, self.y + 100), 100, 2)
    
    def run(self, screen):
        self.move()
        self.render(screen)