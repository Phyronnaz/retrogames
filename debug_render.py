from pygame.rect import Rect

from Quadtree import *
import pygame


def quadtree_render(screen: pygame.Surface, quadtree: Quadtree):
    # print(q.position)
    w = quadtree.width()

    pygame.draw.rect(screen, (0, 255, 0), Rect(quadtree.position, (w, w)), 10)

    if not quadtree.is_leaf:
        for child in quadtree.childs:
            quadtree_render(screen, child)
