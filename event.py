import pygame, sys, gv
from gv import objects

pygame.init()
isClicking = False
mouseMovednot = True
x, y = 0, 0

def main():
    global x, y, isClicking, mouseMovednot
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            isClicking = True
            x, y = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            isClicking = False
            if mouseMovednot:
                x, y = pygame.mouse.get_pos()
                objects.createObj(x, y, (17, 17), 1, "newObject", 0, 0)

            else:
                mouseMovednot = True

            gv.oldX, gv.oldY = -1000, -1000

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gv.playing:
                    gv.playing = False

                else:
                    gv.playing = True

            elif event.key == pygame.K_c:
                objects.clear()

            elif event.key == pygame.K_o:
                name = input("What should this object be called?")
                diameter = int(input("What should be the diameter of this object?"))
                size = (diameter, diameter)
                weight = int(input("How heavy should this object be?"))
                x = int(input("What should be the X coordinate be for this object?")) + 382
                y = int(input("What should be the Y coordinate be for this object?")) + 216
                xVel = int(input("What should be the xVelocity be for this object?"))
                yVel = int(input("What should be the yVelocity be for this object?"))
                objects.createObj(x, y, size, weight, name, xVel, yVel)

            elif event.key == pygame.K_d:
                if len(objects.objects) != 0:
                    objects.objects.pop(len(objects.objects) - 1)

            elif event.key == pygame.K_1:
                x, y = pygame.mouse.get_pos()
                objects.createObj(x, y, (17, 17), 1, "newAttractor", 0, 0)

            elif event.key == pygame.K_2:
                x, y = pygame.mouse.get_pos()
                objects.createObj(x, y, (23, 23), 3, "newAttractor", 0, 0)

            elif event.key == pygame.K_3:
                x, y = pygame.mouse.get_pos()
                objects.createObj(x, y, (23, 23), 3, "newObject", 0, 0)

            elif event.key == pygame.K_4:
                x, y = pygame.mouse.get_pos()
                objects.createObj(x, y, (17, 17), -1, "newObject", 0, 0)

            elif event.key == pygame.K_5:
                x, y = pygame.mouse.get_pos()
                objects.createObj(x, y, (23, 23), -3, "newObject", 0, 0)

            elif event.key == pygame.K_t:
                if gv.drawTrajectory:
                    gv.drawTrajectory = False

                else:
                    gv.drawTrajectory = True

            elif event.key == pygame.K_i:
                if gv.showInstructions:
                    gv.showInstructions = False

                else:
                    gv.showInstructions = True

            elif event.key == pygame.K_f:
                gv.frame = True
                gv.playing = False

        elif event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()