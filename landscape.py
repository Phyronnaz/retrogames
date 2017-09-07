import random
import turtle
import numpy as np
import engine
from config import *
from triangularisation import get_triangle_list_from_polygon


class Landscape(engine.GameObject):
    def __init__(self):
        super().__init__(0, -SCREEN_HEIGHT / 2 + 100, 0, 0, 'landscape', 'yellow')

    def heading(self):
        return 90


def makeshape_landscape():
    def add_middlepoint(start, end, ydiff, depth, divisor):
        if depth == 0:
            return []

        middle = (start + end) / 2 + np.array([0, np.random.random() * ydiff])

        return add_middlepoint(start, middle, ydiff / divisor, depth - 1, divisor) \
               + [middle] \
               + add_middlepoint(middle, end, ydiff / divisor, depth - 1, divisor)

    landscape_shape = turtle.Shape("compound")

    points = [np.array([-SCREEN_WIDTH / 2, 0]), np.array([SCREEN_WIDTH / 2, 0])]
    middle_list = add_middlepoint(points[0], points[1], ydiff=250, depth=6, divisor=1.1)

    polygon = [np.array([-SCREEN_WIDTH / 2, -SCREEN_HEIGHT])] + middle_list + [np.array([SCREEN_WIDTH / 2, -SCREEN_HEIGHT])]
    polygon = [(a[0], a[1]) for a in polygon][::-1]
    triangle_list = get_triangle_list_from_polygon(polygon)
    for triangle in triangle_list:
        landscape_shape.addcomponent(triangle, random.choice(["red","green","blue","orange","purple","pink","yellow"]))


    turtle.register_shape('landscape', landscape_shape)
    return triangle_list
