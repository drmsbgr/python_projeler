# Example file showing a circle moving on screen
import pygame
from Model.CelestialBody import CelestialBody
import random
import copy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

G = 6.6743 * 10e2

b1 = CelestialBody(
    pygame.Vector2(screen.get_width() * 0.5, 50),
    24,
    pygame.Vector2(2 * 3.14 * 40 / 4, 0),
    pygame.Vector2(0, 0),
)

maxStep = 100

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "purple", b1.Position, 20)
    pygame.draw.circle(screen, "purple", pygame.Vector2(screen.get_width()*.5,screen.get_height()*.5), 20)
    Fdir = (
        pygame.Vector2(screen.get_width() * 0.5, screen.get_height() * 0.5)
        - b1.Position
    )

    mBig = 230

    step = 0
    lastPos = copy.copy(b1.Position)
    lastVel = copy.copy(b1.Velocity)

    while step < maxStep:
        dirF = (
            pygame.Vector2(screen.get_width() * 0.5, screen.get_height() * 0.5)
            - lastPos
        )
        FG = G * b1.Mass * mBig * dirF.normalize() / dirF.magnitude_squared()
        lastVel += FG / b1.Mass
        pygame.draw.line(screen, "red", lastPos, lastPos + lastVel)
        lastPos += lastVel
        step += 1

    F = G * mBig * b1.Mass * Fdir.normalize() / Fdir.magnitude_squared()

    b1.Velocity += F / b1.Mass * dt
    b1.Position += b1.Velocity * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
