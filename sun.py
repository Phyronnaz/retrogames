import turtle
import numpy as np
import engine
from config import SCREEN_HEIGHT


class Sun(engine.GameObject):
    def __init__(self):
        super().__init__(0, SCREEN_HEIGHT / 2, 0, 0, 'sun', 'yellow')


def makeshape_sun(scale):
    sun_shape = turtle.Shape("compound")

    shape = []
    n = 100
    for k in range(n):
        x = np.sin(2 * k * np.pi / n)
        y = np.cos(2 * k * np.pi / n)
        shape.append((x, y))

    sun_shape.addcomponent(np.array(shape) * scale, "yellow")

    turtle.register_shape('sun', sun_shape)
