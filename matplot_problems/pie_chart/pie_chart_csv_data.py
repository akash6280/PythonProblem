"""3.Write a Python programming to create a pie chart of gold medal achievements of five most
successful countries in 2016 Summer Olympics."""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(medal_data, labels=country_data, colors=colors,shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n" + "countries in 2016 Summer Olympics")
plt.show()
