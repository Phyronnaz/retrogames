import turtle

import numpy as np

from config import TERRAIN_WIDTH, MAX_DEPTH


class Quadtree:
    def __init__(self, position: np.array, depth: int = 0):
        self.position = np.array(position)  # center
        self.is_leaf = True
        self.childs = []  # type: list(Quadtree)
        self.objects = []
        self.depth = depth

    def width(self):
        return TERRAIN_WIDTH / 2 ** self.depth

    def get_objects(self, position: np.array):
        position = np.array(position)
        if self.is_leaf:
            return self.objects
        else:
            return self.get_child(position).get_objects(position)

    def get_child(self, position: np.array):
        return self.childs[(position[0] >= self.position[0]) + (position[1] >= self.position[1])]

    def is_inside(self, position):
        position = np.array(position)
        return self.position[0] - self.width() / 2 <= position[0] <= self.position[0] + self.width() / 2 \
               and self.position[1] - self.width() / 2 <= position[1] <= self.position[1] + self.width() / 2

    def add_object(self, object):
        d = self.width() / 2
        if object.is_inside(self.position + np.array([-d, -d])) or \
                object.is_inside(self.position + np.array([+d, -d])) or \
                object.is_inside(self.position + np.array([-d, +d])) or \
                object.is_inside(self.position + np.array([+d, +d])) or \
                any([self.is_inside(point) for point in object]):
            if self.depth == MAX_DEPTH:
                self.objects.append(object)
            else:
                if not self.is_leaf:
                    self.is_leaf = False
                    d = self.width() / 4
                    self.childs = [
                        Quadtree(self.position + np.array([-d, -d]), self.depth + 1),
                        Quadtree(self.position + np.array([+d, -d]), self.depth + 1),
                        Quadtree(self.position + np.array([-d, +d]), self.depth + 1),
                        Quadtree(self.position + np.array([+d, +d]), self.depth + 1)
                    ]
                for child in self.childs:
                    child.add_object(object)
