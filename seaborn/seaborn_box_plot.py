"""2. Write a program to draw a box plot of day by tips for a dataset given in a url"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')
# Import Data
tips_dataset = sns.load_dataset("tips")

# Construct plot
sns.boxplot(x="day", y="tip", data=tips_dataset)
plt.show()
