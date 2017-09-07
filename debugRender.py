from Quadtree import *
import pygame

def quadTree_render(screen:pygame.Surface,q:QuadTree):
    print(q.position)
    w=q.width()

    pygame.draw.rect(screen, (0,0,0), Rect((q.position[0],q.position[1]),(w,w)), 1)


    if not q.is_leaf:
        for child in q.childs:
            quadTreeRender(screen, child)