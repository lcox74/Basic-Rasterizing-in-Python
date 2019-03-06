import pygame
import math

class Scene:
    def __init__(self, screen, screen_size, mapFile = "", player = 0):
        self.objects = []
        self.inputObj = []

        self.endScene = True

        self.screen = screen

        self._player = player
        self.AddObject(self._player, True)

        self.fov = 600
        self.far = 100
        
        self.screen_size = screen_size
        self.screen_center = (screen_size[0] // 2, screen_size[1] // 2)

        #Edit
        self.fFov = 90
        self.fNear = 0.1
        self.fFar = 1000
        self.fAspectRatio = screen_size[1]/screen_size[0]
        self.fFovRad = 1 / math.tan(self.fFov * 0.5 / 180 * 3.14159)

        self.mapFile = mapFile
        self.map = []

        self.deltaTime = 0
        self.clock = pygame.time.Clock()

    def AddObject (self, obj, oinput = False):
        self.objects.append(obj)
        if oinput:
            self.inputObj.append(obj)

    def SceneLoop (self):
        self.endScene = False

        while self.endScene == False:
            self.deltaTime = self.clock.tick() / 1000
            self.screen.fill((10, 10, 10))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            keys = pygame.key.get_pressed()
            if len(keys) > 0:
                for o in self.inputObj:
                    o.GetKey(keys)

            self.Update()

            pygame.draw.rect(self.screen, (0, 0, 100), ((0, self.screen_center[1] + 100 ), self.screen_size)) # floor
            drawOrder = sorted(self.objects, key=lambda x: x.GetDistance(), reverse=True)

            for o in drawOrder:
                if o.GetDistance() < self.far:
                    o.Draw()
                    o.LateDraw()

            pygame.display.update()

    def Update(self):
        pass


                