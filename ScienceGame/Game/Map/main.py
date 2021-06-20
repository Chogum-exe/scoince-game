
import pygame
import time

import background

SCREEN_X = 510
SCREEN_Y = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Science Game :D")

    running = True
    FPS = 60

    bgd = background.ScrollingBackround(SCREEN_X, SCREEN_Y)

    x_offset = 0
    y_offset = 0
    count = 0

    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      pygame.display.flip()
      pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))

      bgd.show(screen, x_offset, y_offset)

      x_offset += 1
      y_offset += 1

      time.sleep(1/FPS)

if __name__ == '__main__':
    main()
