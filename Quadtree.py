import numpy as np

from config import TERRAIN_WIDTH


class Quadtree:
    def __init__(self, position: np.array, depth: int = 0):
        self.position = position
        self.is_leaf = True
        self.childs = []  # type: list(Quadtree)
        self.object_position = np.array([0, 0])
        self.callback_object = None
        self.depth = depth

    def width(self):
        return TERRAIN_WIDTH / 2 ** self.depth

    def get_callback_object(self, position: np.array):
        if self.is_leaf:
            return self.callback_object
        else:
            return self.get_child(position).get_callback_object(position)

    def get_child(self, position: np.array):
        return self.childs[(position[0] >= self.position[0]) + (position[1] >= self.position[1])]

    def add_object(self, object_position, callback_object):
        if self.callback_object is None:
            self.callback_object = callback_object
            self.object_position = object_position
        else:
            if self.is_leaf:
                d = self.width() / 4
                self.childs = [
                    Quadtree(self.position + np.array([-d, -d]), self.depth + 1),
                    Quadtree(self.position + np.array([+d, -d]), self.depth + 1),
                    Quadtree(self.position + np.array([-d, +d]), self.depth + 1),
                    Quadtree(self.position + np.array([+d, +d]), self.depth + 1)
                ]
                self.get_child(object_position).add_object(object_position, callback_object)
