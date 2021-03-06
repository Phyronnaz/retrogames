import turtle

import numpy as np
import pygame

from config import *
from game_object import GameObject, DynamicObject


class Rocket(DynamicObject):
    def __init__(self, position=(SCREEN_WIDTH / 2, 0), rotation=np.pi / 2, scale=10):
        super().__init__(position, rotation, scale)

        self.time_since_thrust = 0
        self.corner = [(0, 0), (0, 0)]

        # Engine
        self.orange_shape = np.array(((-1, 0), (-0.75, -1), (-0.5, 0), (-0.25, -1), (0, 0),
                                      (0.25, -1), (0.5, 0), (0.75, -1), (1, 0)))

        self.yellow_shape = np.array(((-1, 0), (-0.75, -0.75), (-0.5, 0), (-0.25, -0.75), (0, 0),
                                      (0.25, -0.75), (0.5, 0), (0.75, -0.75), (1, 0)))

        # Rocket
        self.left_wing_shape = np.array(((-1, 0.25), (-2, 0), (-1.75, 1), (-1, 2)))

        self.right_wing_shape = np.array(((1, 0.25), (2, 0), (1.75, 1), (1, 2)))

        self.main_shape = np.array(((-1, 0.25), (-1, 6), (0, 7.5), (1, 6), (1, 0.25), (0, 0.25)))

    def draw(self, screen):
        if self.time_since_thrust > 0:
            pygame.draw.polygon(screen, (255, 69, 0), self.get_world_position(self.orange_shape), 0)
            pygame.draw.polygon(screen, (255, 215, 0), self.get_world_position(self.yellow_shape), 0)

        pygame.draw.polygon(screen, (0, 0, 0), self.get_world_position(self.left_wing_shape), 0)
        pygame.draw.polygon(screen, (0, 0, 0), self.get_world_position(self.right_wing_shape), 0)
        pygame.draw.polygon(screen, (255, 0, 0), self.get_world_position(self.main_shape), 0)

        pygame.draw.circle(screen, (0, 255, 0), self.corner[0], 5)
        pygame.draw.circle(screen, (0, 255, 0), self.corner[1], 5)

    def update(self, deltatime, events, keys):
        if self.time_since_thrust > 0:
            self.time_since_thrust -= deltatime

        if keys[pygame.K_SPACE]:
            self.acceleration[0] += np.sin(self.rotation) * ROCKET_ACCELERATION_SPEED
            self.acceleration[1] += np.cos(self.rotation) * ROCKET_ACCELERATION_SPEED
            self.time_since_thrust = ROCKET_ENGINE_ANIM_DURATION

        if keys[pygame.K_LEFT]:
            self.angular_acceleration += ROCKET_ANGULAR_ACCELERATION

        if keys[pygame.K_RIGHT]:
            self.angular_acceleration -= ROCKET_ANGULAR_ACCELERATION

        self.acceleration[1] += 100

        super().update(deltatime, events, keys)

    def get_bounding_box_corners(self):

        x1, y1 = self.get_world_position(self.main_shape)[:, 0].min(), self.get_world_position(self.main_shape)[:, 1].min()
        x2, y2 = self.get_world_position(self.main_shape)[:, 0].max(), self.get_world_position(self.main_shape)[:, 1].max()
        self.corner = (int(x1), int(y1)), (int(x2), int(y2))
        return (x1, y1), (x2, y1), (x2, y2), (x1, y2)
