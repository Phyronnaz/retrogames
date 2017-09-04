from collections import deque

def fact(n):
    return n*fact(n-1) if n>0 else 1
def factT(n,acc=1):
    return factT(n-1,n*acc) if n>0 else acc

def bigTrig(l: deque((int,int)))->deque(Triangle):
    res=deque()
    def trig(points: deque((int,int)))->deque((int,int)):
        trig(points)