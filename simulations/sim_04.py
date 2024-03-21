# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

G = -9.8
ballPose = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)
ballMass = 40
ballVelocity = pygame.Vector2(0, 0)
K = 2000
L = 20

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    force = K * (ballPose.distance_to(pygame.mouse.get_pos()) - L) * (
        pygame.mouse.get_pos() - ballPose
    ).normalize() + ballMass * pygame.Vector2(0, G)

    pygame.draw.line(screen, "red", ballPose, ballPose + force)
    pygame.draw.line(screen, "blue", ballPose, ballPose + ballVelocity)

    ballVelocity = 0.99 * ballVelocity + force / ballMass * dt
    ballPose += ballVelocity * dt
    pygame.draw.circle(screen, "blue", ballPose, ballMass)

    if ballPose.y >= screen.get_height() - ballMass or ballPose.y <= ballMass:
        ballVelocity.y *= -1
        ballPose += ballVelocity * dt

    if ballPose.x >= screen.get_width() - ballMass or ballPose.x <= ballMass:
        ballVelocity.x *= -1
        ballPose += ballVelocity * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(144) / 1000  # limits FPS to 144

pygame.quit()
