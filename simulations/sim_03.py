# Example file showing a basic pygame "game loop"
import pygame
import random
from pixel import Pixel

# pygame setup
pygame.init()

size = 256
spacing = 3
pixelSize = 5

n = ((size * 2 + spacing) // (pixelSize + spacing)) ** 2

screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
running = True
dt = 0

amount = 32

pixels = [Pixel(pygame.Vector2(0, 0), 0, "white") for _ in range(n)]

for _ in range(amount):
    i = random.randint(0, len(pixels))
    pixels[i].Value = 1
    pixels[i].Color = "black"

for i, p in enumerate(pixels):
    x = i % n**0.5
    y = i // n**0.5

    p.Position = pygame.Vector2(x * pixelSize * 0.5, y * pixelSize * 0.5)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for p in pixels:
        color = "black" if p.Value == 1 else p.Color
        pygame.draw.rect(
            screen,
            color,
            pygame.Rect(
                p.Position.x * 2 + spacing,
                p.Position.y * 2 + spacing,
                pixelSize,
                pixelSize,
            ),
        )

    for p1 in pixels:
        minDist = 999999
        targetP = p1
        for p2 in pixels:
            if p1 == p2 or p2.Value != 1:
                continue
            dist = p1.Position.distance_to(p2.Position)
            if dist <= minDist:
                minDist = dist
                targetP = p2
        v = minDist / size / 2**0.5 * 255
        p1.Color = (v, v, v)
        # pygame.draw.line(screen, "black", p1.Position, targetP.Position)

    for p in pixels:
        if p.Value == 1:
            p.Position += (
                pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5)) * dt
            )

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(20) / 1000  # limits FPS to 144

pygame.quit()
