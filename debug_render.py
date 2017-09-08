from pygame.rect import Rect

from Quadtree import *
from game_object import *
from config import *

class QuadtreeRender(GameObject):
    def __init__(self, quadtree: Quadtree):
        self.quadtree = quadtree
        super().__init__()

    def quadtree_render(self, screen: pygame.Surface, quadtree: Quadtree):
        w = quadtree.width() * self.engine.global_scale

        rand = np.random.RandomState(int(quadtree.position[0] + quadtree.position[1] * TERRAIN_WIDTH) + TERRAIN_WIDTH * TERRAIN_WIDTH)
        color = (rand.randint(0, 256), rand.randint(0, 256), rand.randint(0, 256))

        rect = Rect(self.get_world_position(quadtree.position) - np.ones(2) * w / 2, (w, w))
        pygame.draw.rect(screen, color, rect, 2)

        # for object in quadtree.objects:
        #     pygame.draw.polygon(screen, color, [self.get_world_position(p) for p in object])

        if not quadtree.is_leaf:
            for child in quadtree.childs:
                gPos=self.get_world_position(child.position)
                if 0 <= gPos[0]+w/2 and gPos[0]-w/2 <= SCREEN_WIDTH and 0 <= gPos[1]+w/2 and gPos[0]-w/2 <= SCREEN_HEIGHT and w > 100:
                    self.quadtree_render(screen, child)

    def draw(self, screen):
        self.quadtree_render(screen, self.quadtree)
