import turtle
import numpy as np
import ../engine
from Rocket.config import *


class Landscape(engine.GameObject):
    def __init__(self):
        super().__init__(0, -HEIGHT / 2 + 100, 0, 0, 'landscape', 'yellow')

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

    points = [np.array([-WIDTH / 2, 0]), np.array([WIDTH / 2, 0])]
    list = add_middlepoint(points[0], points[1], ydiff=250, depth=5, divisor=2)

    landscape_shape.addcomponent(np.array([np.array([-WIDTH / 2, -HEIGHT])] + list + [np.array([WIDTH / 2, -HEIGHT])]),
                                 "grey")

    turtle.register_shape('landscape', landscape_shape)
