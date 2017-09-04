import turtle

import time

import engine
import numpy as np

from config import *


class Rocket(engine.GameObject):
    def __init__(self, engine):
        self.speed = np.zeros(2)
        self.acceleration = np.zeros(2)

        self.engine = engine
        self.rocket_engine = None
        self.timer = 0
        self.angle = 90

        super().__init__(0, 0, 0, 0, 'rocket', 'red')

    def move(self):
        self.speed += 0.1 * self.acceleration

        self.x += self.speed[0] * 0.1
        self.y += self.speed[1] * 0.1

        self.acceleration = np.array([0, -9.8])

        self.timer += 1
        if self.timer > 100 and self.rocket_engine is not None:
            self.engine.del_obj(self.rocket_engine)
            self.rocket_engine = None

        if self.rocket_engine is not None:
            self.rocket_engine.x = self.x
            self.rocket_engine.y = self.y
            self.rocket_engine.angle = self.angle

        if (HEIGHT / 2 - self.y) ** 2 + self.x ** 2 < 10000 and False:
            self.banner("Game Over")
            self.x = 0
            self.y = 0
            self.speed[:] = 0
            self.acceleration[:] = 0
            self.angle = 90

        if np.abs(self.x) > WIDTH / 2:
            self.speed[0] *= - 1
        if np.abs(self.y) > HEIGHT / 2:
            self.speed[1] *= - 1

    def keyboard(self, key):
        if key == 'space':
            self.acceleration[0] += 100 * np.cos(np.radians(self.angle))
            self.acceleration[1] += 100 * np.sin(np.radians(self.angle))

            if self.rocket_engine is None:
                self.rocket_engine = RocketEngine()
                self.engine.add_obj(self.rocket_engine)
                self.timer = 0
        elif key == 'Left':
            self.angle -= 1
        elif key == 'Right':
            self.angle += 1

    def heading(self):
        return self.angle

    def isoob(self):
        return False

    def banner(self, message):
        turtle.home()
        turtle.color('black')
        turtle.write(message, True, align='center', font=('Arial', 48, 'italic'))
        time.sleep(3)
        turtle.undo()


class RocketEngine(engine.GameObject):
    def __init__(self):
        self.angle = 90
        super().__init__(0, 0, 0, 0, 'rocket_engine', 'orange')

    def heading(self):
        return self.angle


def makeshape_rocket(scale: float):
    # Rocket engine
    rocket_engine_shape = turtle.Shape("compound")
    orange_shape = np.array(((-1, 0), (-0.75, -1), (-0.5, 0), (-0.25, -1), (0, 0),
                             (0.25, -1), (0.5, 0), (0.75, -1), (1, 0)))
    yellow_shape = np.array(((-1, 0), (-0.75, -0.75), (-0.5, 0), (-0.25, -0.75), (0, 0),
                             (0.25, -0.75), (0.5, 0), (0.75, -0.75), (1, 0)))

    rocket_engine_shape.addcomponent(orange_shape * scale, "orange")
    rocket_engine_shape.addcomponent(yellow_shape * scale, "yellow")

    turtle.register_shape('rocket_engine', rocket_engine_shape)

    # Rocket
    rocket_shape = turtle.Shape("compound")
    left_wing = np.array(((-1, 0.25), (-2, 0), (-1.75, 1), (-1, 2)))
    right_wing = np.array(((1, 0.25), (2, 0), (1.75, 1), (1, 2)))
    main = np.array(((-1, 0.25), (-1, 6), (0, 7.5), (1, 6), (1, 0.25), (0, 0.25)))

    rocket_shape.addcomponent(left_wing * scale, "black")
    rocket_shape.addcomponent(right_wing * scale, "black")
    rocket_shape.addcomponent(main * scale, "red")

    turtle.register_shape('rocket', rocket_shape)
