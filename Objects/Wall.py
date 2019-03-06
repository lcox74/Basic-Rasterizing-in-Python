import pygame
from Objects.Object import Object

class Wall(Object):
    def __init__ (self, scene, colour = (255, 255, 255), pos = (0, 0, 10), rot = (0, 0, 0)):
        Object.__init__(self, scene, 'Wall', colour, pos, rot)
        self.AddPoints((1, 1, 1))       #0
        self.AddPoints((-1, 1, 1))      #1
        self.AddPoints((-1, 1, -1))     #2
        self.AddPoints((1, 1, -1))      #3
        self.AddPoints((1, -1, 1))      #4
        self.AddPoints((-1, -1, 1))     #5
        self.AddPoints((-1, -1, -1))    #6
        self.AddPoints((1, -1, -1))     #7

        self.AddFace([0, 1, 5, 4])
        self.AddFace([0, 3, 7, 4])
        self.AddFace([6, 5, 1, 2])
        self.AddFace([6, 7, 3, 2])

        self.setImage("StoneB.png")





