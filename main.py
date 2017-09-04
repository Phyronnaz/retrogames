from config import *
from landscape import *
from rocket import *
from sun import *

makeshape_rocket(10)
makeshape_sun(100)
makeshape_landscape()

engine.init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
engine.init_engine()

sun = Sun()
landscape = Landscape()
rocket = Rocket(engine)

engine.add_obj(sun)
engine.add_obj(landscape)
engine.add_obj(rocket)

engine.set_keyboard_handler(rocket.keyboard)
engine.engine()
