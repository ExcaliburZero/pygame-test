"""The the module that handles the interface window."""
import pygame
import sys
from pygame.locals import *

# Setup window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test!")

# Do some drawing
images_dir = "resources/images/"
image_location_panel_normal = images_dir + "panel_normal.png"
image_panel_normal = pygame.image.load(image_location_panel_normal)

# Draw panels
for x in range(3):
    for y in range(3):
        DISPLAYSURF.blit(image_panel_normal, (((x + 1) * 40), ((y + 1) * 25)))

# Main game loop
while True:
    for event in pygame.event.get():
        # End the program if the user quits
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Update the display
        pygame.display.update()
