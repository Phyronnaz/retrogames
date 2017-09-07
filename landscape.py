import numpy as np
import pygame

from config import *
from game_object import StaticObject
from triangularisation import get_triangle_list_from_polygon


class Landscape(StaticObject):
    def __init__(self, color=(0, 0, 0, 0), width=0):
        super().__init__((0, 0))
        self.triangle_list = []
        self.polygon = []
        self.color = color
        self.width = width
        self.create()

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, np.add(self.polygon, self.position), self.width)

    def create(self):
        def add_middlepoint(start, end, ydiff, depth, divisor):
            if depth == 0:
                return []

            middle = (start + end) / 2 + np.array([0, np.random.random() * ydiff])

            return add_middlepoint(start, middle, ydiff / divisor, depth - 1, divisor) \
                   + [middle] \
                   + add_middlepoint(middle, end, ydiff / divisor, depth - 1, divisor)

        points = [np.array([-TERRAIN_WIDTH / 2, TERRAIN_MEAN]), np.array([TERRAIN_WIDTH / 2, TERRAIN_MEAN])]
        middle_list = add_middlepoint(points[0], points[1], ydiff=250, depth=8, divisor=1.5)

        points = [np.array([-TERRAIN_WIDTH / 2, TERRAIN_HEIGHT / 2 + TERRAIN_MEAN])] + \
                 middle_list + \
                 [np.array([TERRAIN_WIDTH / 2, TERRAIN_HEIGHT / 2 + TERRAIN_MEAN])]

        rotation_matrix = np.array([[np.cos(self.rotation), -np.sin(self.rotation)],
                                    [np.sin(self.rotation), np.cos(self.rotation)]])

        self.polygon = [tuple(p.dot(rotation_matrix) + self.position) for p in points]

        self.triangle_list = get_triangle_list_from_polygon(self.polygon)

    def get_components(self):
        return self.triangle_list
