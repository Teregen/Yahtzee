import pygame
import random
from constants import *






def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    cursor_surface = pygame.Surface((20, 20), pygame.SRCALPHA) #create a surface for the cursor
    cursor_surface.set_colorkey((0, 0, 0)) #set the color key to black
    cursor_surface.fill((0, 0, 0, 255)) #fill the surface with black
    cursor = pygame.cursors.Cursor((10, 10), cursor_surface) #create a cursor from the surface
    pygame.mouse.set_cursor(cursor) #set the cursor to the custom cursor



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #exit game if the user closes the window
        screen.fill((0, 110, 0))
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000





if __name__ == "__main__":
    main()