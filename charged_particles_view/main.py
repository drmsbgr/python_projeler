from PIL import Image
from PIL import ImageColor
import random
import math


class Particle:

    def __init__(self, x, y, charge):
        self.x = x
        self.y = y
        self.charge = charge


n = 9
width = 2**n
height = 2**n
randomParticlesCount = 256

img = Image.new("RGB", (width, height), (255, 255, 255))

particles = []

for p in range(0, randomParticlesCount):
    randX = random.randint(0, width - 1)
    randY = random.randint(0, height - 1)
    randCharge = random.randint(-20, 20)
    particles.append(Particle(randX, randY, randCharge))
    img.putpixel((randX, randY), (255, 255, 255))

k = 2

for x in range(0, width):
    for y in range(0, height):
        v = 0
        for item in particles:
            p: Particle = item
            if p.x == x and p.y == y:
                continue
            v -= p.charge / math.sqrt(math.pow((p.x - x), 2) + math.pow((p.y - y), 2))

        if v < 0:
            img.putpixel((x, y), (int(abs(v) * 128 / k), 0, 0))
        elif v > 0:
            img.putpixel((x, y), (0, 0, int(abs(v) * 255 / k)))
        else:
            img.putpixel((x, y), (255, 255, 255))
img.show()
