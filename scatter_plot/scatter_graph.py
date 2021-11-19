
"""1.Write a Python program to draw a scatter graph taking a random distribution in X and Y and
plotted against each other."""
import matplotlib.pyplot as plt
from pylab import randn

X = randn(50)
Y = randn(50)
print(X)
plt.scatter(X, Y, color='b')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
