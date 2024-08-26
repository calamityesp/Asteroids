import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, dt):
        pygame.draw.circle(self.position, self.radius, 2)
