import pygame

# width height of window
pygame.display.set_mode((400, 500))

# background surface color
surface = pygame.display.get_surface()

color = (20, 20, 20)
surface.fill(color)
pygame.display.flip()
