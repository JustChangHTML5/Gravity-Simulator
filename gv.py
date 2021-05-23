import pygame
from simulation import Simulation

objects = Simulation()

pygame.init()

playing = True
frame = False
pygame.display.set_caption("Gravity Simulator", "GS")
Icon = pygame.image.load("Game\GameIcon.png")
pygame.display.set_icon(Icon)