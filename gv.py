import pygame
from simulation import Simulation

objects = Simulation()

pygame.init()

playing = True
frame = False
screen = None
pygame.display.set_caption("Gravity Simulator", "GS")
Icon = pygame.image.load("Game\GameIcon.png")
pygame.display.set_icon(Icon)
font = pygame.font.SysFont("comicsansms", 17)
font2 = pygame.font.SysFont("comicsansms", 13)