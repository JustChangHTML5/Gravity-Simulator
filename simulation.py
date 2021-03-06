import pygame, math, gv
from ast import literal_eval

def drawWords():
    if gv.playing:
        playingDisplay = gv.font.render("Playing", 1, pygame.Color("green"))

    else:
        playingDisplay = gv.font.render("Not Playing", 1, pygame.Color("red"))

    objectDisplay = gv.font.render(str(len(gv.objects.objects)) + " Objects", 1, pygame.Color("black"))

    if gv.showInstructions:
        Instructions = gv.font2.render('Click to place a normal object, 1 for attractor, 2 for heavy attractor, 3 for heavy object, 4 for negative mass object, 5 for "heavy" negative mass object. Hit t to show trajectories, d to undo, c to clear, and i to stop showing the instructions.', 1, pygame.Color("black"))

    gv.screen.blit(playingDisplay, (5, 0))
    gv.screen.blit(objectDisplay, (110, 0))
    if gv.showInstructions:
        gv.screen.blit(Instructions, (200, 0))

class Object(pygame.sprite.Sprite):
    def __init__(self, mX, mY, objSize, weight, name, xVel, yVel):
        super().__init__()
        self.objSize = objSize
        self.radius = objSize[0] // 2
        self.name = name
        self.weight = weight
        self.vX = xVel
        self.vY = yVel
        self.mX = mX
        self.mY = mY
        self.object = pygame.image.load("Game\Object.png")
        self.object = pygame.transform.smoothscale(self.object, objSize)
        self.objRect = self.object.get_rect()
        self.objRect.x = self.mX - self.radius
        self.objRect.y = self.mY - self.radius

    def changePos(self, x, y):
        self.mX += x
        self.mY += y
        self.objRect.x = self.mX - self.radius
        self.objRect.y =self.mY - self.radius

    def move(self):
        self.mX += self.vX
        self.mY += self.vY
        self.objRect.x = self.mX - self.radius
        self.objRect.y = self.mY - self.radius

    def simulate(self, obj2):
        distance = math.sqrt(abs(self.mX - obj2.mX) ** 2 + abs(self.mY - obj2.mY) ** 2)
        self.mX += self.vX
        self.mY += self.vY
        if distance != 0:
            try:
                ratioWhole = abs(self.mX - obj2.mX) + abs(self.mY - obj2.mY)
                pullFactor = obj2.weight * self.weight * obj2.weight/distance
                xPull = pullFactor * ((obj2.mX - self.mX) / ratioWhole) * 0.14159
                yPull = pullFactor * ((obj2.mY - self.mY) / ratioWhole) * 0.14159
                self.vX += xPull
                self.vY += yPull
            except:
                pass
            #notice how positive mass is attracted to negative mass in 2d but repeled in 3d.

        self.objRect.x = self.mX - self.radius
        self.objRect.y = self.mY - self.radius

class Simulation:
    def __init__(self):
        self.objects = []
        self.attracters = []

    def createObj(self, x, y, size, weight, name, xvel, yvel):
        newObject = Object(x, y, size, weight, name, xvel, yvel)
        self.objects.append(newObject)

    def deleteObj(self, name):
        for object in self.objects:
            if object.name == name:
                self.objects.remove(object)

    def clear(self):
        self.objects.clear()

    def blitObjects(self, screen):
        for object in self.objects:
            screen.blit(object.object, object.objRect)

    def simulateManual(self, obj1, obj2, lockNot):
        obj1.simulate(obj2)
        if lockNot:
            obj2.simulate(obj1)

    def simulateAuto(self):
        if len(self.objects) == 1 and self.objects[0].name != "newAttractor":
            self.objects[0].move()

        else:
            for object in self.objects:
                for object2 in self.objects:
                    if object != object2 and object.name != "newAttractor":
                        self.simulateManual(object, object2, False)

    def move(self, x, y):
        for object in self.objects:
            object.changePos(x, y)

    def drawTrajectory(self):
        for object in self.objects:
            pygame.draw.line(gv.screen, pygame.Color("black"), (object.objRect.x + object.radius, object.objRect.y + object.radius), (object.mX + object.vX * 37, object.mY + object.vY * 37), 3)

    def save(self):
        saveList = []
        for object in self.objects:
            saveList.append((object.mX, object.mY, object.objSize, object.weight, object.name, object.vX, object.vY))

        saveFile = open("Game\simulation.txt", "w")
        saveFile.write(repr(saveList))
        saveFile.close()

    def load(self):
        dataFile = open("Game\simulation.txt", "r")
        data = dataFile.read()
        dataFile.close()
        data = literal_eval(data)
        self.clear()
        for object in data:
            self.createObj(object[0], object[1], object[2], object[3], object[4], object[5], object[6])