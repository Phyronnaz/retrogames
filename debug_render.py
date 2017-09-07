from pygame.rect import Rect

from Quadtree import *
import pygame


def quadtree_render(screen: pygame.Surface, q: Quadtree):
    print(q.position)
    w = q.width()

    pygame.draw.rect(screen, (0, 0, 0), Rect(q.position, (w, w)), 0)

    if not q.is_leaf:
        for child in q.childs:
            quadtree_render(screen, child)
