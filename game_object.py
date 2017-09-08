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

    def get_collision(self) -> (str, object):
        pass

    def move(self, delta_pos):
        delta_pos = np.array(delta_pos)
        self.position += delta_pos

    def get_world_position(self, position):
        position = np.array(position)
        rotation_matrix = np.array([[np.cos(self.rotation), -np.sin(self.rotation)],
                                    [np.sin(self.rotation), np.cos(self.rotation)]])

        return self.engine.global_scale * np.add(self.scale * np.dot(
            position, rotation_matrix), self.position) + self.engine.global_position


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

    def get_bounding_box(self) -> ((int, int), (int, int)):
        pass

    def update(self, deltatime, events, keys):
        self.speed += deltatime * self.acceleration
        self.position += deltatime * self.speed
        self.acceleration = np.zeros(2)
        self.rotation += self.angular_speed * deltatime
        self.angular_speed += self.angular_acceleration * deltatime
        self.angular_acceleration = 0
