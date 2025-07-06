import pygame

pygame.init()
info = pygme.display.Info()
SCREEN_WIDTH = 1920
SCREEN_HEIGT = 1080
FPS = 60

GAME_PLAYING = 0
GAME_OVER = 1

run = True
while run:
    clock.tick(FPS)

    pygame.display.update()
pygame.quit()