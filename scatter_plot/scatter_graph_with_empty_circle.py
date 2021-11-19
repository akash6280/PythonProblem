"""2.Write a Python program to draw a scatter plot with empty circles taking a random distribution
in X and Y and plotted against each other"""
import matplotlib.pyplot as plt
from pylab import randn
x = randn(50)
y = randn(50)
plt.scatter(x, y, s=70, facecolors='none', edgecolors='r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
