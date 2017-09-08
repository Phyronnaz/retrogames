from debug_render import QuadtreeRender
from engine import Engine
from landscape import Landscape
from rocket import Rocket

engine = Engine()
engine.global_scale = 0.1
engine.add_static_object(Landscape())
engine.add_game_object(QuadtreeRender(engine.quadtree))
engine.add_dynamic_object(Rocket())


engine.loop()