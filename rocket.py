import turtle

import numpy as np
import pygame

from config import SCREEN_WIDTH
from game_object import GameObject, DynamicObject


class Rocket(DynamicObject):
    def __init__(self, scale=10):
        super().__init__((SCREEN_WIDTH / 2, 100))

        self.orange_shape = np.array(((-1, 0), (-0.75, -1), (-0.5, 0), (-0.25, -1), (0, 0),
                                      (0.25, -1), (0.5, 0), (0.75, -1), (1, 0))) * scale
        self.yellow_shape = np.array(((-1, 0), (-0.75, -0.75), (-0.5, 0), (-0.25, -0.75), (0, 0),
                                      (0.25, -0.75), (0.5, 0), (0.75, -0.75), (1, 0))) * scale

        # Rocket
        self.left_wing_shape = np.array(((-1, 0.25), (-2, 0), (-1.75, 1), (-1, 2))) * scale
        self.right_wing_shape = np.array(((1, 0.25), (2, 0), (1.75, 1), (1, 2))) * scale
        self.main_shape = np.array(((-1, 0.25), (-1, 6), (0, 7.5), (1, 6), (1, 0.25), (0, 0.25))) * scale

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 69, 0), np.add(self.orange_shape, self.position), 0)
        pygame.draw.polygon(screen, (255, 215, 0), np.add(self.yellow_shape, self.position), 0)

        pygame.draw.polygon(screen, (0, 0, 0), np.add(self.left_wing_shape, self.position), 0)
        pygame.draw.polygon(screen, (0, 0, 0), np.add(self.right_wing_shape, self.position), 0)
        pygame.draw.polygon(screen, (255, 0, 0), np.add(self.main_shape, self.position), 0)

    def update(self, events):
        pass
