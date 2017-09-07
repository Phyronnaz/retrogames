import pygame


class GameObject:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self, events):
        pass

    def get_collision(self) -> (str, object):
        pass

class StaticObject(GameObject):
    def is_inside(self, position: (int, int)) -> bool:
        pass


class DynamicObject(GameObject):
    def get_bounding_box(self) -> ((int, int), (int, int)):
        pass