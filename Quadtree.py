import numpy as np

from config import TERRAIN_WIDTH, MAX_DEPTH


class Quadtree:
    def __init__(self, position: np.array, depth: int = 0):
        self.position = position  # center
        self.is_leaf = True
        self.childs = []  # type: list(Quadtree)
        self.triangles = []
        self.depth = depth

    def width(self):
        return TERRAIN_WIDTH / 2 ** self.depth

    def get_triangles(self, position: np.array):
        if self.is_leaf:
            return self.triangles
        else:
            return self.get_child(position).get_triangles(position)

    def get_child(self, position: np.array):
        return self.childs[(position[0] >= self.position[0]) + (position[1] >= self.position[1])]

    def add_triangle(self, triangle):
        d = self.width() / 2
        if triangle.is_inside(self.position + np.array([-d, -d])) or \
                triangle.is_inside(self.position + np.array([+d, -d])) or \
                triangle.is_inside(self.position + np.array([-d, +d])) or \
                triangle.is_inside(self.position + np.array([+d, +d])):

            if self.depth == MAX_DEPTH:
                self.triangles.append(triangle)
            else:
                self.is_leaf = False
                d = self.width() / 4
                self.childs = [
                    Quadtree(self.position + np.array([-d, -d]), self.depth + 1),
                    Quadtree(self.position + np.array([+d, -d]), self.depth + 1),
                    Quadtree(self.position + np.array([-d, +d]), self.depth + 1),
                    Quadtree(self.position + np.array([+d, +d]), self.depth + 1)
                ]
                for child in self.childs:
                    child.add_triangle(triangle)
