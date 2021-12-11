"""1.Write a Python programming to create a pie chart of the popularity of programming Languages."""
import matplotlib.pyplot as plt

languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# Plot
plt.pie(popularity, labels=languages, colors=colors, startangle=140)

plt.show()
