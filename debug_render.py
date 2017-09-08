from pygame.rect import Rect

from Quadtree import *
from game_object import *


class QuadtreeRender(GameObject):
    def __init__(self, quadtree: Quadtree):
        self.quadtree = quadtree
        super().__init__()

    def quadtree_render(self, screen: pygame.Surface, quadtree: Quadtree):
        w = quadtree.width() * self.engine.global_scale
         
        rect = Rect(self.get_world_position(quadtree.position) - np.ones(2) * w / 2, (w,  w))
        pygame.draw.rect(screen, (0, 255, 0), rect, 1)

        if not quadtree.is_leaf:
            for child in quadtree.childs:
                self.quadtree_render(screen, child)

    def draw(self, screen):
        self.quadtree_render(screen, self.quadtree)
