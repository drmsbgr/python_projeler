from PIL import Image
from PIL import ImageColor
import random
import math

n = 9
width = 2**n
height = 2**n
randomPointsCount = 64

img = Image.new("RGB", (width, height), (255, 255, 255))

points = []

for p in range(randomPointsCount):
    randX = random.randint(0, width - 1)
    randY = random.randint(0, height - 1)
    points.append([randX, randY, int(p / randomPointsCount * 180)])
    img.putpixel((randX, randY), (0, 0, 0))

for x in range(width):
    for y in range(height):
        closestPoint = points[0]
        for p in points:
            if p != closestPoint:
                distToClosest = math.sqrt(
                    (closestPoint[0] - x) ** 2 + (closestPoint[1] - y) ** 2
                )
                distToCurrent = math.sqrt((p[0] - x) ** 2 + (p[1] - y) ** 2)
                if distToClosest > distToCurrent:
                    closestPoint = p
        img.putpixel(
            xy=(x, y),
            value=ImageColor.getrgb(
                f"hsv({min(100, int(distToClosest))}, 100% , 100%)"
            ),
        )
img.show()
img.save("voronoi_texture.png", "png")
