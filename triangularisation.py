from collections import deque
from triangle import *
from cycleList import *


def fact(n):
    return n * fact(n - 1) if n > 0 else 1


def factT(n, acc=1):
    return factT(n - 1, n * acc) if n > 0 else acc


def is_convex(p1,p2,p3):
    pass



def get_first_ear(c:CycleList)->(int,int):
    def is_convex(d,o,b):
        return True
    
    for e in c:
        triangle=Triangle(e.previous_node.data,e.data,e.next_node.data)
        if triangle.is_valide():
            continue
        if triangle.some_inside(map(lambda y:y.data,filter(lambda x: x.data not in triangle ,c))):
            continue
        else:
            return e,triangle

def trig(l:list())->list():
    c=CycleList()
    for e in l:
        c.push(l)
    
    triangleList=[]

    for _ in range(len(l)-2):
        ear,triangle=get_first_ear(c)
        triangleList.append(triangle)
        c.remove(ear)

    return triangleList

print("caca")
print(get_first_ear(CycleList().push((0,0)).push((10,0)).push((0,10)).push((1,1)).push((10,10))))