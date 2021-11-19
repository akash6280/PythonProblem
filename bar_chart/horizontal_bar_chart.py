"""2.Write a Python programming to display a horizontal bar chart of the popularity of
programming Languages."""
import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, val in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of Programming Language")
plt.yticks(x_pos, x)
plt.show()