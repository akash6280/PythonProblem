"""1. Write a program to draw bar plot of sex against survived for a dataset given in the url"""
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')
# Import Data
titanic_dataset = sns.load_dataset("titanic")

# Construct plot
sns.barplot(x="sex", y="survived", hue="pclass",data=titanic_dataset)
plt.show()
