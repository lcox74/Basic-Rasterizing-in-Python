import pygame

class EnvObj:
    def __init__ (self, pos, color, res, symb):
        self.pos = pos
        self.color = color
        self.s = symb

    def Draw (self, screen):
        pygame.draw.circle(screen, self.color, self.pos, 3)

pygame.init()

sSize = (800, 600)
screen = pygame.display.set_mode(sSize, pygame.DOUBLEBUF, 32)

clock = pygame.time.Clock()


resolution = 10

curPos = (resolution//2, resolution//2)
fixPos = (0, 0)

curMap = ['_'] * int(sSize[0]//resolution * sSize[1]//resolution)


EnvList = []

pygame.key.set_repeat()

while True:
    clock.tick(30)
    screen.fill((10, 10, 10))
    
    keys = pygame.key.get_pressed()
    if len(keys) > 0:
        if keys[pygame.K_UP] and keys[pygame.K_LSHIFT] and curPos[1] > resolution/2:
            curPos = (curPos[0], curPos[1] - resolution)
            fixPos = (fixPos[0], fixPos[1] - 1)
        if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT] and curPos[1] < sSize[1] - resolution/2:
            curPos = (curPos[0], curPos[1] + resolution)
            fixPos = (fixPos[0], fixPos[1] + 1)
        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT] and curPos[0] > resolution/2:
            curPos = (curPos[0] - resolution, curPos[1])
            fixPos = (fixPos[0] - 1, fixPos[1])
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT] and curPos[0] < sSize[0] - resolution/2:
            curPos = (curPos[0] + resolution, curPos[1])
            fixPos = (fixPos[0] + 1, fixPos[1])
        if keys[pygame.K_q]:
            
            tx,ty = 0, 0
            file = open("[Temp]map.txt", "w")
            while ty < sSize[1]//resolution:
                charl = ""
                while tx < sSize[0]//resolution:
                    charl += curMap[sSize[0]//resolution * ty + tx]
                    tx += 1
                print(charl)
                tx = 0
                ty += 1
                file.write(charl + '\n')

            file.close()

        if keys[pygame.K_SPACE]:
            if curMap[int(sSize[0]//resolution * fixPos[1] + fixPos[0])] != '#':
                curMap[int(sSize[0]//resolution * fixPos[1] + fixPos[0])] = '#'
                EnvList.append(EnvObj(curPos, (0, 200, 0), resolution//2, '#'))
        if keys[pygame.K_p]:
            if curMap[int(sSize[0]//resolution * fixPos[1] + fixPos[0])] != 'P':
                curMap[int(sSize[0]//resolution * fixPos[1] + fixPos[0])] = 'P'
                EnvList.append(EnvObj(curPos, (0, 0, 200), resolution//2, 'P'))
        if keys[pygame.K_e]:
            curMap[int(sSize[0]//resolution * fixPos[1] + fixPos[0])] = '_'
            x = 0
            while x < len(EnvList):
                if EnvList[x].pos == curPos:
                    EnvList.remove(EnvList[x])
                x += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                curPos = (curPos[0], curPos[1] - resolution)
                fixPos = (fixPos[0], fixPos[1] - 1)
            if e.key == pygame.K_DOWN:
                curPos = (curPos[0], curPos[1] + resolution)
                fixPos = (fixPos[0], fixPos[1] + 1)
            if e.key == pygame.K_LEFT:
                curPos = (curPos[0] - resolution, curPos[1])
                fixPos = (fixPos[0] - 1, fixPos[1])
            if e.key == pygame.K_RIGHT:
                curPos = (curPos[0] + resolution, curPos[1])
                fixPos = (fixPos[0] + 1, fixPos[1])

    for w in EnvList:
        w.Draw(screen)

    pygame.draw.circle(screen, (255, 255, 255), curPos, 2)
    pygame.display.update()





