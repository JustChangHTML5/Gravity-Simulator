import pygame, event, gv
from simulation import drawWords

pygame.init()
screen = pygame.display.set_mode((1000, 571), pygame.RESIZABLE)
gv.screen = screen
objects = gv.objects
gv.oldX, gv.oldY = -1000, -1000

clock = pygame.time.Clock()

def main():
    while True:
        screen.fill((230, 230, 230))
        clock.tick(60)

        if gv.playing or gv.frame:
            objects.simulateAuto()
            gv.frame = False

        objects.blitObjects(screen)

        event.main()

        if event.isClicking:
            if abs(event.x - gv.oldX) >= 1 or abs(event.y - gv.oldY) >= 1:
                if gv.oldX != -1000 and gv.oldY != -1000:
                    event.mouseMovednot = False
                    gv.objects.move((event.x - gv.oldX), (event.y - gv.oldY))
                gv.oldX, gv.oldY = event.x, event.y
            event.x, event.y = pygame.mouse.get_pos()

        drawWords()
        if gv.drawTrajectory:
            objects.drawTrajectory()

        pygame.display.flip()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
