import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

data = pd.read_csv("HR-Employee-Attrition.csv")
data_attr_yes = data[data.Attrition == 'Yes']
data_attr_no = data[data.Attrition == 'No']

data_pie = data.Attrition.value_counts()
plt.pie(data_pie, labels=data_pie.index, autopct='%1.1f%%')

x = ["Low", "Medium", "High", "Very High"]
plt.figure(figsize=(12, 6))
plt.title('Environment Satisfaction Distribution')
plt.xlabel('Environment Satisfaction')
plt.ylabel('Number of Employees')
plt.hist(data.EnvironmentSatisfaction, label='Attrition')
y_pos = [1, 2, 3, 4]
plt.xticks(y_pos, x)
plt.show()

job_involvement_data = data["JobInvolvement"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
plt.pie(data.JobInvolvement.value_counts(), labels=x, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')
plt.title("Job involvement Distribution")
plt.show()

sns.countplot(x="JobSatisfaction", hue="Attrition", data=data)
plt.show()


fig, ax = plt.subplots(1, 2, figsize=(16, 4))
sns.distplot(data["PerformanceRating"],ax=ax[0])
sns.distplot(data["RelationshipSatisfaction"], ax=ax[1])
plt.show()
plt.show()
