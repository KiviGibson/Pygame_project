import pygame

title = "Game Title"
icon = ""
# width height of window
pygame.display.set_mode((400, 500))

# background surface color
surface = pygame.display.get_surface()

color = (20, 20, 20)
surface.fill(color)
pygame.display.flip()

# setting window name
pygame.display.set_caption(title)
if icon != "":
    IconImage = pygame.image.load(icon)
    pygame.display.set_icon(IconImage)
