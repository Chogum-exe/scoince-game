from .controller import KeyHandler
from ...sheetloader import SpriteLoader
import os

class Player:
    def __init__(self, x, y, pygame):
        pygame.init()
        self.size = 144
        sheet = SpriteLoader(os.path.join(".","Game","Player","Frames","PlayerFrames.png"), (self.size*2, self.size))
        self.sprites = sheet.images_at([(0, 0, 1728, 1728), (0, 1728, 1728, 3456)], -1)
        self.x = x
        self.y = y
        self.pygame = pygame
        self.controller = KeyHandler(self.pygame)

    def move(self):
        x_dir, y_dir = self.controller.wasd()
        self.x += x_dir
        self.y += y_dir

    def render(self, screen):
        frame = self.pygame.Rect(self.x, self.y, self.size, self.size)
        screen.blit(self.sprites[0], (self.x, self.y), frame)
    
    def run(self, screen):
        self.move()
        self.render(screen)