import pygame, event, gv

pygame.init()
screen = pygame.display.set_mode((765, 432), pygame.RESIZABLE)
objects = gv.objects

clock = pygame.time.Clock()

def main():
    while True:
        screen.fill((230, 230, 230))
        clock.tick(60)
        """
        if len(objects.objects) == 2:
            objects.simulateManual(objects.objects[0], objects.objects[1], False)
            objects.simulateManual(objects.objects[1], objects.objects[0], False)
        """
        if gv.playing or gv.frame:
            objects.simulateAuto()
            gv.frame = False
        objects.blitObjects(screen)

        event.main()
        pygame.display.flip()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
