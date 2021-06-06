from .controller import KeyHandler
from ...sheetloader import SpriteLoader
import os

class Player:
    def __init__(self, x, y, pygame):
        pygame.init()
        self.x = x
        self.y = y
        self.pygame = pygame
        self.controller = KeyHandler(self.pygame)

    def move(self):
        x_dir, y_dir = self.controller.wasd()
        self.x += x_dir
        self.y += y_dir

    def render(self, screen):
        sheet = SpriteLoader(os.path.join(".","Game","Player","Frames","PlayerFrames.png"))
        sprites = sheet.images_at([(0, 0, 1728, 1728), (0, 1728, 1728, 3456)])
        screen.blit(sprites[0], (self.x, self.y))
        # self.pygame.draw.circle(screen, (234,63,74), (self.x + 100, self.y + 100), 100, 2)
    
    def run(self, screen):
        self.move()
        self.render(screen)