import pygame

from Quadtree import Quadtree
from config import *


class Engine:
    def __init__(self):
        self.quadtree = Quadtree((0, 0))
        self.static_objects = []
        self.dynamic_objects = []

    def add_static_object(self, static_object):
        self.static_objects.append(static_object)

    def add_dynamic_object(self, dynamic_object):
        self.dynamic_objects.append(dynamic_object)

    def start(self):
        # Initialize the game engine
        pygame.init()

        # Define the colors we will use in RGB format
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        # Set the height and width of the screen
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("retrogames")

        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()

        while not done:

            # This limits the while loop to a max of 10 times per second.x
            # Leave this out and we will use all CPU we can.
            clock.tick(60)

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            # Clear the screen and set the screen background
            screen.fill(WHITE)

            for game_object in self.static_objects + self.dynamic_objects:
                game_object.update()
                game_object.draw()

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()
