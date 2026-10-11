import matplotlib.pyplot as plt
import numpy as np
import cmath

t = np.linspace(-2, 2, 1024)

data2d = np.exp(t[:, np.newaxis] * t[np.newaxis, :])

fig, ax = plt.subplots()
im = ax.imshow(data2d, cmap="jet")
ax.set_title("deneme")

fig.colorbar(im, ax=ax, label="Interactive colorbar")

plt.show()
