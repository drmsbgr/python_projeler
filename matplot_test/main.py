import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] ** 2 + np.cos(t)[np.newaxis, :] ** 3

fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title("deneme")

fig.colorbar(im, ax=ax, label="Interactive colorbar")

plt.show()
