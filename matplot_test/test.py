import matplotlib.pyplot as plt


def dortgen_ciz(startx, starty, width, heigth):
    # verilen x ve y noktalarına çizgi çizer
    x = [startx, startx + width, startx + width, startx, startx]
    y = [starty, starty, starty + heigth, starty + heigth, starty]
    plt.plot(x, y)


dortgen_ciz(5, 5, 10, 2)
dortgen_ciz(0, 0, 4, 4)

plt.show()