"""The the module that handles the interface window."""
import pygame
import sys
from pygame.locals import *

# Setup window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test!")

# Do some drawing
pygame.draw.line(DISPLAYSURF, (249, 0, 0), (60, 60), (120, 60), 4)

# Main game loop
while True:
    for event in pygame.event.get():
        # End the program if the user quits
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Update the display
        pygame.display.update()
