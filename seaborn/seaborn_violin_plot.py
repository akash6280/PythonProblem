"""Write a program to draw a violin plot of “sex” against “total bill” for a dataset given in a url"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')
# Import Data
tips_dataset = sns.load_dataset("tips")

# Construct plot
sns.violinplot(x="sex", y="total_bill", hue="day", data=tips_dataset)
plt.show()
