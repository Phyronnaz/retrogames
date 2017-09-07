from engine import Engine
from landscape import Landscape

engine = Engine()
engine.add_static_object(Landscape())
engine.start()