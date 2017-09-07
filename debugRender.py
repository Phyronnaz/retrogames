from Quadtree import *
import pygame

def quadTreeRender(screen:pygame.Surface,q:QuadTree):
    print(self.position)
    w=q.width()/2
    x1=self.position[0]-w
    x2=self.position[0]+w
    y1=self.position[1]-w
    y2=self.position[1]+w

    pygame.draw.line(screen, (0,0,0), (x1,y1), (x1,y2), width=1)
    pygame.draw.line(screen, (0,0,0), (x1,y2), (x2,y2), width=1)
    pygame.draw.line(screen, (0,0,0), (x2,y2), (x2,y1), width=1)
    pygame.draw.line(screen, (0,0,0), (x2,y1), (x2,y1), width=1)


    if not q.is_leaf:
        for child in q.childs:
            quadTreeRender(screen, child)