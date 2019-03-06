import pygame

from Scenes.mainScene import mainScene

pygame.init()

sSize = (800, 600)

screen = pygame.display.set_mode(sSize, pygame.DOUBLEBUF, 32)

Scenes = []
Scenes.append(mainScene(screen, sSize, "[Temp]map.txt"))

while True:

    screen.fill((10, 10, 10))
    pygame.display.update()

    for s in Scenes:
        s.SceneLoop()