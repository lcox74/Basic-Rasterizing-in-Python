import pygame
import pygame.gfxdraw
from pygame.locals import *
import time
import math
import os

class Object:
    def __init__(self, scene, _type, colour = (255, 255, 255), pos = (1, 1, 1), rot = (0, 0, 0)):
        self.pos = pos
        self.rot = rot

        self.colour = colour
        self.originalC = colour
        self._type = _type

        self.scene = scene

        self.points = []
        self.faces = []

        self.image = 0

    def setImage (self, img):
        self.image = pygame.image.load(os.path.join('Images', img))

    def AddPoints(self, point):
        self.points.append(point)

    def AddFace (self, ps):
        self.faces.append(ps)

    def rotateY (self, pos, radian):
        x,y = pos
        s,c = math.sin(radian), math.cos(radian)
        return x * c - y * s, y * c + x * s

    def normalise (self, point):
        x, y, z = point
        w = math.sqrt(x**2 + y**2 + z**2)
        if w != 0:
            return (x/w, y/w, z/w)
        else:
            return (0, 0, 0.1)

    def dot (self, point1, point2):
        return point1[0] * point2[0] + point1[1] * point2[1] + point1[2] * point2[2]

    def projectionTo2D (self, x, y, z):
        x = x + self.pos[0] - self.scene._player.pos[0]
        y = y + self.pos[1] - self.scene._player.pos[1]
        z = z + self.pos[2] - self.scene._player.pos[2]

        x, z = self.rotateY ((x, z), math.radians(self.scene._player.rot[1]))
        if z == 0: z = 0.1
        f = self.scene.fov / z
        x,y = x * f, y * f

        return (int(x) + self.scene.screen_center[0], int(y) + self.scene.screen_center[0])

    def Draw(self):
        self.Update()

        if len(self.points) > 0:
            nPoints = []
            curPoint = 0
            for x, y, z in self.points:
                nx, ny = self.projectionTo2D(x, y, z)

                nPoints.append((nx, ny))
                curPoint += 1

            a, b, c = self.pos
            x, y, z = self.scene._player.pos

            if self.dot(self.normalise((a - x, b - y, c - z)), self.scene._player.getDirection()) > 0.56:
                for f in self.faces:
                    face = [nPoints[f[0]], nPoints[f[1]], nPoints[f[2]], nPoints[f[3]]]

                    # if self.image == 0:
                    tempC = self.LerpC((10, 10, 10), self.colour, 1-(self.GetDistance())/self.scene.far*2)
                    pygame.draw.polygon(self.scene.screen, tempC, face)
                    # else:
                    #     print (self.scene.screen, face, self.image, -1, -1)
                    #     pygame.gfxdraw.textured_polygon(self.scene.screen, face, self.image, -1, -1)

    def GetDistance (self):
        a, b, c = self.pos
        x, y, z = self.scene._player.pos

        return math.sqrt((x - a)**2 + (y - b)**2 + (z - c)**2)

    def GetKey (self, key):
        pass

    def Update (self):
        pass

    def LateDraw(self):
        pass

    def Lerp (self, s, e, t):
        if t < 0:
            t = 0
        elif t > 1:
            t = 1
        return (1 - t) * s + e * t

    def LerpC (self, sc, ec, t):
        return (self.Lerp(sc[0], ec[0], t), self.Lerp(sc[1], ec[1], t), self.Lerp(sc[2], ec[2], t))
