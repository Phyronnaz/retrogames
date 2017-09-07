import numpy as np
import pygame

from config import *
from game_object import StaticObject
from triangularisation import get_triangle_list_from_polygon


class Landscape(StaticObject):
    def __init__(self, color=(0, 0, 0, 0), width=1):
        super().__init__((0, 0))
        self.triangle_list = []
        self.polygon = []
        self.color = color
        self.width = width
        self.create()

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.polygon, self.width)

    def create(self):
        def add_middlepoint(start, end, ydiff, depth, divisor):
            if depth == 0:
                return []

            middle = (start + end) / 2 + np.array([0, np.random.random() * ydiff])

            return add_middlepoint(start, middle, ydiff / divisor, depth - 1, divisor) \
                   + [middle] \
                   + add_middlepoint(middle, end, ydiff / divisor, depth - 1, divisor)

        points = [np.array([-SCREEN_WIDTH / 2, 0]), np.array([SCREEN_WIDTH / 2, 0])]
        middle_list = add_middlepoint(points[0], points[1], ydiff=250, depth=6, divisor=1.1)

        polygon = [np.array([-SCREEN_WIDTH / 2, -SCREEN_HEIGHT])] + middle_list + [
            np.array([SCREEN_WIDTH / 2, -SCREEN_HEIGHT])]

        self.polygon = [(a[0], a[1]) for a in polygon][::-1]
        self.triangle_list = get_triangle_list_from_polygon(self.polygon)
