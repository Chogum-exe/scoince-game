from .controller import KeyHandler
from ...sheetloader import SpriteLoader
import os

class Player:
    def __init__(self, x, y, pygame):
        pygame.init()
        sheet = SpriteLoader(os.path.join(".","Game","Player","Frames","PlayerFrames.png"), (144, 288))
        self.sprites = sheet.images_at([(0, 0, 1728, 1728), (0, 1728, 1728, 3456)])
        self.x = x
        self.y = y
        self.pygame = pygame
        self.controller = KeyHandler(self.pygame)

    def move(self):
        x_dir, y_dir = self.controller.wasd()
        self.x += x_dir
        self.y += y_dir

    def render(self, screen):
        screen.blit(self.sprites[0], (self.x, self.y))
    
    def run(self, screen):
        self.move()
        self.render(screen)