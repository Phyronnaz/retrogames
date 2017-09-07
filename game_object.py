import numpy as np
import pygame


class GameObject:
    def __init__(self, position=(0, 0), rotation=0):
        self.position = np.array(position)
        self.rotation = rotation

    def draw(self, screen):
        pass

    def update(self, events):
        pass

    def get_collision(self) -> (str, object):
        pass

    def move(self, delta_pos):
        delta_pos = np.array(delta_pos)
        self.position += delta_pos


class StaticObject(GameObject):
    def __init__(self, position=(0, 0), rotation=0):
        super().__init__(position, rotation)

    def is_inside(self, position: (int, int)) -> bool:
        pass

    def get_components(self):
        pass


class DynamicObject(GameObject):
    def __init__(self, position=(0, 0), rotation=0, speed=(0, 0)):
        super().__init__(position, rotation)
        self.speed = np.array(speed)

    def get_bounding_box(self) -> ((int, int), (int, int)):
        pass

    def update(self, events):
        pass
