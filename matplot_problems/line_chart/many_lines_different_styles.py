"""11. Write a Python program to plot several lines with different format styles in one command
using arrays."""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
plt.show()