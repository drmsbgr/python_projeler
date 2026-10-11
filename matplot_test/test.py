import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(-1, 1, 1024)
data2d = (
    t[:, np.newaxis] ** 3 * t[np.newaxis, :] + t[:, np.newaxis] * t[np.newaxis, :] ** 2
)
data3 = 5 * np.exp(t[:, np.newaxis] ** 2 + t[np.newaxis, :] ** 2)

fig, ax = plt.subplots()
im = ax.imshow(data3, cmap="jet")
ax.set_title("deneme")

fig.colorbar(im, ax=ax, label="Interactive colorbar")

plt.show()
