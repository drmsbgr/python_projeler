import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout="constrained")
plt.plot(x, x, label="doğrusal")  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label="kuadratik")  # etc.
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.title("iki fonksiyonun kesişimi")
plt.legend()
plt.show()
