import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 1, 1024)


y = 3 * t + 4

fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1)

im = ax1.plot(t, y)

ax1.set_title("elektrik alan")

#fig.colorbar(im, ax=ax1, label="renk paleti")

plt.show()
