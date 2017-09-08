import numpy as np
import pygame


class GameObject:
    def __init__(self, position=(0, 0), rotation=0, scale=1):
        self.position = np.array(position, dtype=float)
        self.rotation = rotation
        self.scale = scale
        self.engine = None

    def draw(self, screen):
        pass

    def get_world_position(self, position):
        position = np.array(position)
        rotation_matrix = np.array([[np.cos(self.rotation), -np.sin(self.rotation)],
                                    [np.sin(self.rotation), np.cos(self.rotation)]])

        return self.engine.global_scale * (np.add(self.scale * np.dot(position, rotation_matrix), self.position) + \
               self.engine.global_position)


class StaticObject(GameObject):
    def __init__(self, position=(0, 0), rotation=0, scale=1):
        super().__init__(position, rotation, scale)

    def is_inside(self, position: (int, int)) -> bool:
        pass

    def get_components(self):
        pass


class DynamicObject(GameObject):
    def __init__(self, position=(0, 0), rotation=0, scale=1, speed=(0, 0)):
        super().__init__(position, rotation, scale)
        self.speed = np.array(speed, dtype=float)
        self.acceleration = np.zeros(2)
        self.angular_speed = 0
        self.angular_acceleration = 0
        self.last_position = np.zeros(2)

    def get_bounding_box_corners(self) -> ((int, int), (int, int), (int, int), (int, int)):
        pass

    def update(self, deltatime, events, keys):
        self.last_position = self.position

        self.speed += deltatime * self.acceleration
        self.position += deltatime * self.speed
        self.acceleration = np.zeros(2)
        self.rotation += self.angular_speed * deltatime
        self.angular_speed += self.angular_acceleration * deltatime
        self.angular_acceleration = 0

    def is_inside(self, position):
        (x1, y1), (x2, y1), (x2, y2), (x1, y2) = self.get_bounding_box_corners()

        return x1 <= position[0] <= x2 and y1 <= position[0] <= y2

    def collide_with(self, object):
        type, collision = object.get_collision()

        corners = self.get_bounding_box_corners()
        (x1, y1), (x2, y1), (x2, y2), (x1, y2) = corners

        def is_inside(position):
            return x1 <= position[0] <= x2 and y1 <= position[0] <= y2

        if type == "triangle":
            triangle = collision
            collide = False
            for corner in corners:
                if triangle.is_inside((corner - self.engine.global_position) / self.engine.global_scale):
                    collide = True
                    break
            for p in triangle:
                if is_inside(p):
                    collide = True
                    break
            if collide:
                print("Collide")
                p0 = np.array(triangle.p0)
                p1 = np.array(triangle.p1)
                p2 = np.array(triangle.p2)
                side1 = np.array(p1 - p0)
                side2 = np.array(p2 - p1)
                side3 = np.array(p0 - p2)

                side1_l = []
                side2_l = []
                side3_l = []
                for corner in corners:
                    side1_l.append((np.array(corner) - p0).dot(side1))
                    side2_l.append((np.array(corner) - p1).dot(side2))
                    side3_l.append((np.array(corner) - p2).dot(side3))

                side1_m = max(side1_l)
                side2_m = max(side2_l)
                side3_m = max(side3_l)

                if side1_m < side2_m and side1_m < side3_m:
                    side = side1
                elif side2_m < side1_m and side2_m < side3_m:
                    side = side2
                elif side3_m < side1_m and side3_m < side2_m:
                    side = side3

                theta = np.arctan2(side[1], side[0])
                reflection_matrix = np.array([[np.cos(2 * theta), np.sin(2 * theta)],
                                              [np.sin(2 * theta), -np.cos(2 * theta)]])

                self.position = self.last_position
                self.speed = self.speed.dot(reflection_matrix)

    def __iter__(self):
        for t in self.get_bounding_box_corners():
            yield np.array(t)
