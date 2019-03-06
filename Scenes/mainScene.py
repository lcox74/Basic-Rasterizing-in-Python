from Scenes.Scene import Scene
from Objects.Wall import Wall
from Objects.Player import Player
from Objects.Light import Light

class mainScene(Scene):
    def __init__(self, screen, screen_size, mapFile = ""):

        _player = Player(self, (0, 0, -5))
        Scene.__init__(self, screen, screen_size, mapFile, _player)

        self.InstanciateMap()

    def InstanciateMap (self):
        file = open(self.mapFile, "r").read()
        self.map = file.split('\n')

        pos = (1000, 0, 1000)
        ix, iy, iz = pos
        for z in self.map:
            for x in z:
                if x == "#":
                    self.AddObject(Wall(self, (20, 120, 50), pos))
                if x == "P":
                    self._player.pos = pos
                if x == "L":
                    self.AddObject(Light(self, (100, 200, 260), pos))
                pos = (pos[0] + 2, iy, pos[2])
            pos = (ix, iy, pos[2] - 2)

    def Update (self):
        #self.focal = (self.focal[0], self.focal[1], self.focal[2] + 1/120)
        pass


