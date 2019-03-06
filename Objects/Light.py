import pygame, math
from Objects.Object import Object

class Light(Object):
    def __init__(self, scene, colour = (255, 255, 255), pos = (0, 0, 0), rot = (0, 0, 0)):
        Object.__init__(self, scene, 'Light', colour, pos, rot)
        self.maxRange = 8
        self.intensity = 20


    def Update(self):
        for o in self.scene.objects:
            if o._type == "Wall" and self.Distance(self.pos, o.pos) <= self.maxRange:
                o.colour = self.LerpC(o.originalC, self.colour, self.Distance(self.pos, o.pos)/self.maxRange * self.intensity * self.scene.deltaTime)

    def Distance(self, s, e):
        return math.sqrt((e[0] - s[0])**2 + (e[1] - s[1])**2 + (e[2] - s[2])**2)