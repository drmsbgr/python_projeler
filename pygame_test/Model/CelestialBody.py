import pygame


class CelestialBody:

    def __init__(
        self, pos: pygame.Vector2, mass: float, vel: pygame.Vector2, acc: pygame.Vector2
    ):
        super(CelestialBody, self).__init__()
        self.Position = pos
        self.Mass = mass
        self.Velocity = vel
        self.Acceleration = acc

    def AddForce(self, force: pygame.Vector2, dt):
        self.Velocity += force / self.Mass * dt
