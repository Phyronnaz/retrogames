import numpy as np
import pygame

from Quadtree import Quadtree
from config import *


class Engine:
    def __init__(self):
        self.quadtree = Quadtree((0, 0))
        self.static_objects = []
        self.dynamic_objects = []
        self.game_objects = []
        self.global_scale = 1
        self.global_position = np.zeros(2)

    def add_static_object(self, static_object):
        static_object.engine = self
        self.static_objects.append(static_object)
        for component in static_object.get_components():
            self.quadtree.add_object(component)

    def add_dynamic_object(self, dynamic_object):
        dynamic_object.engine = self
        self.dynamic_objects.append(dynamic_object)

    def add_game_object(self, game_object):
        game_object.engine = self
        self.game_objects.append(game_object)

    def loop(self):
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
            deltatime = 1 / 60

            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LCTRL]:
                if keys[pygame.K_LEFT]:
                    self.global_position[0] += 10
                if keys[pygame.K_RIGHT]:
                    self.global_position[0] -= 10
                if keys[pygame.K_DOWN]:
                    self.global_position[1] -= 10
                if keys[pygame.K_UP]:
                    self.global_position[1] += 10
                if keys[pygame.K_EQUALS] or keys[pygame.K_KP_PLUS]:
                    self.global_scale *= 1 + 0.01
                if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:
                    self.global_scale *= 1 - 0.01

            for event in events:  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            # Clear the screen and set the screen background
            screen.fill(WHITE)

            if not keys[pygame.K_LCTRL]:
                for dynamic_object in self.dynamic_objects:
                    dynamic_object.update(deltatime, events, keys)

                for dynamic_object in self.dynamic_objects:
                    for objects in [self.quadtree.get_objects(p) for p in dynamic_object]:
                        for object in objects:
                            dynamic_object.collide_with(object)

            for game_object in self.static_objects + self.dynamic_objects + self.game_objects:
                game_object.draw(screen)

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()
