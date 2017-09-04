# basic moving box

import turtle
import engine
import numpy as np

WIDTH = 960
HEIGHT = 1080


class Box(engine.GameObject):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 'turtle', 'red')
        self.speed = 0

    def move(self):
        self.y -= self.speed
        self.speed += 0

    def keyboard_cb(self, key):
        if key == 'space':
            print("Space")
            self.speed -= 1

    def heading(self):
        return 90

if __name__ == '__main__':
    engine.init_screen(WIDTH, HEIGHT)
    engine.init_engine()
    box = Box()
    engine.add_obj(box)
    engine.set_keyboard_handler(box.keyboard_cb)
    engine.engine()
