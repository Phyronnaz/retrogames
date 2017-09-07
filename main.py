from engine import Engine
from landscape import Landscape
from rocket import Rocket

engine = Engine()
engine.add_static_object(Landscape())
engine.add_dynamic_object(Rocket())
engine.start()