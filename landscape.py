import numpy as np
import pygame

from config import *
from game_object import StaticObject
from triangularisation import get_triangle_list_from_polygon


class Landscape(StaticObject):
    def __init__(self, color=(0, 0, 0, 0), width=0):
        super().__init__((0, 0))
        self.triangle_list = []
        self.polygons = []
        self.color = color
        self.width = width
        self.create()

    def draw(self, screen):
        for polygon in self.polygons:
            pygame.draw.polygon(
                screen,
                self.color,
                self.get_world_position(
                    polygon),
                self.width)

    def create(self):
        def add_middlepoint(start, end, ydiff, depth, divisor):
            if depth == 0:
                return []
            height = np.random.random() * ydiff
            middle = (start + end) / 2 + np.array([0, height])

            return add_middlepoint(start,
                                   middle,
                                   ydiff / divisor,
                                   depth - 1,
                                   divisor) + [middle] + add_middlepoint(middle,
                                                                         end,
                                                                         ydiff / divisor,
                                                                         depth - 1,
                                                                         divisor)

        points = [np.array([-TERRAIN_WIDTH / 2, TERRAIN_MEAN]),
                  np.array([TERRAIN_WIDTH / 2, TERRAIN_MEAN])]
        middle_list = add_middlepoint(
            points[0],
            points[1],
            ydiff=LANDSCAPE_MAX_HILL_SIZE,
            depth=LANDSCAPE_DEPTH,
            divisor=LANDSCAPE_HEIGHT_DIVISOR)

        chunked_list = [middle_list[e *
                                    CHUNK_SIZE:(e +
                                                1) *
                                    CHUNK_SIZE] for e in range(TERRAIN_WIDTH //
                                                               CHUNK_SIZE)]

        self.polygons = [[np.array([e[0][0], TERRAIN_HEIGHT / 2 + TERRAIN_MEAN])] +
                        e +
                        [np.array([e[-1][0], TERRAIN_HEIGHT / 2 + TERRAIN_MEAN])]
                        for e in chunked_list]

        self.triangle_list = get_triangle_list_from_polygon(
            ([tuple(p) for polygon in self.polygons for p in polygon]))

    def get_components(self):
        return self.triangle_list
