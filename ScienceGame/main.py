#!/usr/bin/env python3
import pygame
import numpy
# import time

# from Game.Questions.Question import *

# print(GenerateQuestions('Multiple', 'Computer', 1, 0))
# from Game.Player.Python.player import Player

pygame.init()

window = (1000, 562)
screen = pygame.display.set_mode(window, pygame.DOUBLEBUF)
pygame.Surface(window)
WIDTH, HEIGHT = screen.get_size()

pygame.display.set_caption("Science Game :D")

loadingImage = pygame.image.load('loading.png')
# screen.blit(loadingImage, (0, 0))
# pygame.display.flip()
# Display the background instead of a blank screen

programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

button1 = pygame.image.load('button1.png')
button1Width, button1Height = button1.get_size()
button1X = (window[0] / 2) - button1Width / 2
button1Y = 300
button1Rect = pygame.draw.rect(screen, [255, 255, 255], [button1X, button1Y, button1Width, button1Height], False)
# pygame.draw.rect((button1X, button1Y), (0,0,0), (button1Width, button1Height))

button2 = pygame.image.load('button2.png')
button2Height, button2Width = button2.get_size()
button2X = (window[0] / 2) - button2Width
button2Y = 300



c = pygame.time.Clock()

running = True
loadingScreen = True
game = False
FPS = 60




while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.blit(loadingImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print('d')
            if button1Rect.collidepoint(mouseX, mouseY):
                down = True
            else:
                down = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print('u')
            if down == True:
                up = True
        else:
            up = False


    if button1Rect.collidepoint(mouseX, mouseY):
        screen.blit(button2, (button2X, button2Y))
        if up == True:
            running = False
            Game = True
        # elif down == True:
        #
        #     # if down = True do some kind of button down animation
    else:
        # screen.blit(button2, (button2X, button2Y))
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #         makeAPressedVersionOfButton = True
        #         print('d')
        #     elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        #         print('u')
        #         running = False
        #         Game = True
        # else:
            screen.blit(button1, (button1X, button1Y))

            # for s in all_sprites:
            #     s.check_click(event.pos)
    # screen.blit(button1, (Button1X, 300))
    # pygame.display.update()

    pygame.display.flip()

    c.tick(20)
    # if pygame.mouse.get_pressed()[0] and

    while game:
        game = exit()
        c.tick(60)
        # Run it in

  # pygame.display.flip()
  # screen.fill((0,255,255))
  # c.tick(3)
