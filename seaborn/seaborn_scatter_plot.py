"""Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')
# Import Data
tips_dataset = sns.load_dataset("tips")

# Construct plot
sns.pointplot(x="day", y="total_bill", data=tips_dataset)
plt.show()
