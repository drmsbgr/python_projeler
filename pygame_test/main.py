# Example file showing a circle moving on screen
import pygame
from Model.CelestialBody import CelestialBody
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

spawnAmount = 5

bodies = []

for _ in range(spawnAmount):
    randomPose = pygame.Vector2(
        random.randint(0, screen.get_width()), random.randint(0, screen.get_height())
    )
    randomMass = random.randint(10, 20)
    bodies.append(
        CelestialBody(randomPose, randomMass, pygame.Vector2(), pygame.Vector2())
    )

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerVel = pygame.Vector2(0, 0)

G = 6.6743 * 10e4
playerMass = 30
playerForce = 900
playerAcc = playerForce / playerMass

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, playerMass)
    pygame.draw.line(screen, "white", player_pos, player_pos + playerVel, 1)

    for body in bodies:
        distToPlayer = player_pos.distance_to(body.Position)
        playerForce = (
            G
            * playerMass
            * body.Mass
            / distToPlayer**2
            * (player_pos - body.Position)
            / distToPlayer
        )

        if distToPlayer < 40:
            playerForce = pygame.Vector2(0, 0)

        body.AddForce(playerForce, dt)
        body.Position += body.Velocity * dt
        pygame.draw.circle(screen, "blue", body.Position, body.Mass)
        pygame.draw.line(
            screen, "white", body.Position, body.Position + body.Velocity, 1
        )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerVel.y -= playerAcc * dt
    if keys[pygame.K_s]:
        playerVel.y += playerAcc * dt
    if keys[pygame.K_a]:
        playerVel.x -= playerAcc * dt
    if keys[pygame.K_d]:
        playerVel.x += playerAcc * dt

    player_pos += playerVel * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
