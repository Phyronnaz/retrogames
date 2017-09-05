from collections import deque
from triangle import *
from cycleList import *


def fact(n):
    return n * fact(n - 1) if n > 0 else 1


def factT(n, acc=1):
    return factT(n - 1, n * acc) if n > 0 else acc


def is_convex(p1,p2,p3):
    pass



def get_first_ear(c:CycleList):
    def is_convex(d,o,b):
        return True
    def format(e:Node):
        tmp=(e.previous_node.data,e.data,e.next_node.data)
        return (tmp)+(filter(lambda x: x!=tmp[0] and x!=tmp[1] and x!=tmp[2] ,c))
    for e in c:
        tmp=Triangle(e.previous_node.data,e.data,e.next_node.data)
        if tmp.is_convex():
            continue
        elif tmp.some_inside(map(lambda y:y.data,filter(lambda x: x!=tmp[0] and x!=tmp[1] and x!=tmp[2] ,c))):
            continue
        else:
            return tmp
    


get_first_ear(CycleList().push((0,0)).push((10,0)).push((0,10)).push((1,1)).push((10,10)))