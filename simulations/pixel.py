import pygame


class Pixel:
    def __init__(self, pos: pygame.Vector2, value: int, color):
        super(Pixel, self).__init__()
        self.Value = value
        self.Color = color
        self.Position = pos
