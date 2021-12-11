"""1. Write a program to draw a swarm plot of total bill against size for a given dataset"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')
# Import Data
tips_dataset = sns.load_dataset("tips")

# Construct plot
sns.boxplot(x="total_bill", y="size", data=tips_dataset)
plt.show()
