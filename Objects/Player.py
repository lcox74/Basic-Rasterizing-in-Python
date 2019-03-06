import pygame, math
from Objects.Object import Object
from Objects.Bullet import Bullet

class Player(Object):
    def __init__(self, scene, pos = (0, 0, 0), rot = (0, 0, 0)):
        Object.__init__(self, scene, 'Player',(0, 0, 0), pos, rot)

        self.speed = 5
        self.sensitivity = 100

        self.collisionR = 1

    def normalise (self, point):
        x, y, z = point
        w = math.sqrt(x**2 + y**2 + z**2)
        return (x/w, y/w, z/w)

    def getDirection (self):
        return (math.sin(math.radians(self.rot[1])), 0, math.cos(math.radians(self.rot[1])))

    def GetKey (self, key):
        if key[pygame.K_LEFT]:
            self.rot = (self.rot[0], self.rot[1] - self.sensitivity * self.scene.deltaTime, self.rot[2])
        if key[pygame.K_RIGHT]:
            self.rot = (self.rot[0], self.rot[1] + self.sensitivity * self.scene.deltaTime, self.rot[2])

        x, z = self.speed * math.sin(math.radians(self.rot[1])) * self.scene.deltaTime, self.speed * math.cos(math.radians(self.rot[1])) * self.scene.deltaTime
        
        if key[pygame.K_UP] and not self.Collision(self.pos[0] + x, self.pos[2] + z):
            self.pos = (self.pos[0] + x, self.pos[1], self.pos[2] + z)
        if key[pygame.K_DOWN] and not self.Collision(self.pos[0] - x, self.pos[2] - z):
            self.pos = (self.pos[0] - x, self.pos[1], self.pos[2] - z)
        if key[pygame.K_PAGEUP] and not self.Collision(self.pos[0] - x, self.pos[2] + z):
            self.pos = (self.pos[0] - z, self.pos[1], self.pos[2] + x)
        if key[pygame.K_PAGEDOWN] and not self.Collision(self.pos[0] + x, self.pos[2] - z):
            self.pos = (self.pos[0] + z, self.pos[1], self.pos[2] - x)

    def Collision (self, nx, nz):
        nx *= self.collisionR
        nz *= self.collisionR
        
        for o in self.scene.objects:
            if o._type == "Wall":
                if nx < o.pos[0] + 1.5 and nx > o.pos[0] - 1.5 and nz < o.pos[2] + 1.5 and nz > o.pos[2] - 1.5:
                    return True
                # if math.sqrt((o.pos[0] - nx)**2 + (o.pos[2] - nz)**2) < 1:
                #     return False
        return False


    def GetForward(self, dist):
        x, z = dist * math.sin(math.radians(self.rot[1])) * self.scene.deltaTime, dist * math.cos(math.radians(self.rot[1])) * self.scene.deltaTime
        return (self.pos[0] + x, self.pos[1], self.pos[2] + z)
        

    def Update (self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.scene.AddObject(Bullet(self.scene, self.GetForward(1), self.rot))


    def LateDraw(self):
        pygame.draw.rect(self.scene.screen, (200,200,200), ((self.scene.screen_center[0] - 45, self.scene.screen_size[1] - 130), (90, 120)))
