import pygame, math

class Object(pygame.sprite.Sprite):
    def __init__(self, mX, mY, objSize, weight, name, xVel, yVel):
        super().__init__()
        self.name = name
        self.weight = weight
        self.vX = xVel
        self.vY = yVel
        self.mX = mX
        self.mY = mY
        self.object = pygame.image.load("Game\Object.png")
        self.object = pygame.transform.smoothscale(self.object, objSize)
        self.objRect = self.object.get_rect()
        self.objRect.center = (mX, mY)

    def move(self):
        self.mX += self.vX
        self.mY += self.vY
        self.objRect.x = self.mX
        self.objRect.y = self.mY

    def simulate(self, obj2):
        distance = math.sqrt(abs(self.mX - obj2.mX) ** 2 + abs(self.mY - obj2.mY) ** 2)
        self.mX += self.vX
        self.mY += self.vY
        if distance != 0:
            ratioWhole = abs(self.mX - obj2.mX) + abs(self.mY - obj2.mY)
            pullFactor = obj2.weight * self.weight * obj2.weight/distance
            xPull = pullFactor * ((obj2.mX - self.mX) / ratioWhole) * 0.1
            yPull = pullFactor * ((obj2.mY - self.mY) / ratioWhole) * 0.1
            self.vX += xPull
            self.vY += yPull

        self.objRect.x = self.mX
        self.objRect.y = self.mY

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