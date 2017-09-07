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

    def add_triangle(self, triangle):
        d = self.width() / 2
        if triangle.is_inside(self.position + np.array([-d, -d])) or \
                triangle.is_inside(self.position + np.array([+d, -d])) or \
                triangle.is_inside(self.position + np.array([-d, +d])) or \
                triangle.is_inside(self.position + np.array([+d, +d])) or \
                self.is_inside(triangle[0]) or \
                self.is_inside(triangle[1]) or \
                self.is_inside(triangle[2]):
                if self.depth == MAX_DEPTH:
                    self.objects.append(triangle)
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

    def draw(self):
        print(self.position)
        turtle.goto(self.position[0], self.position[1])
        turtle.shapesize(0.1, 0.1, 0.1)
        turtle.shape("square")
        turtle.color("red" if len(self.objects) == 0 else "black")
        turtle.stamp()
        turtle.shapesize(1, 1, 1)


        if not self.is_leaf:
            for child in self.childs:
                child.draw()