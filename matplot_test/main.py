import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(-4, 4 * np.pi, 1024)
data2d = np.exp(-np.cos(t)**2)[:, np.newaxis] * np.exp(-np.sin(t)**2)[np.newaxis, :]

fig, ax = plt.subplots()
im = ax.imshow(data2d, cmap="jet")
ax.set_title("deneme")

fig.colorbar(im, ax=ax, label="Interactive colorbar")

plt.show()
