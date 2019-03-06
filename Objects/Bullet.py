import pygame, math
from Objects.Object import Object

class Bullet(Object):
    def __init__(self, scene, pos = (0, 0, 0), rot = (0, 0, 0)):
        Object.__init__(self, scene, 'Bullet', (0, 0, 0), pos, rot)
        self.speed = 10
        self.colour = (255, 255, 255)
        self.timer = 5

    def Update(self):
        self.timer -= self.scene.deltaTime
        if self.timer < 0:
            self.scene.objects.remove(self)

        dx, dz = self.speed * math.sin(math.radians(self.rot[1])) * self.scene.deltaTime, self.speed * math.cos(math.radians(self.rot[1])) * self.scene.deltaTime
        self.pos = (self.pos[0] + dx, self.pos[1], self.pos[2] + dz)

        x = self.pos[0] - self.scene._player.pos[0]
        y = self.pos[1] - self.scene._player.pos[1]
        z = self.pos[2] - self.scene._player.pos[2]

        x, z = self.rotateY ((x, z), math.radians(self.scene._player.rot[1]))
        if z == 0: z = 0.001
        f = self.scene.fov / z
        x,y = x * f, y * f

        a, b, c = self.pos
        px, py, pz = self.scene._player.pos

        if self.dot(self.normalise((a - px, b - py, c - pz)), self.scene._player.getDirection()) > 0.67:
            tempC = self.LerpC((10, 10, 10), self.colour, 1-(self.GetDistance())/self.scene.far*2)
            size = int(self.Lerp(1, 10, 1-(self.GetDistance())/self.scene.far * 5))
            pygame.draw.circle(self.scene.screen, tempC, (int(x) + self.scene.screen_center[0], int(y) + self.scene.screen_center[0]), size)