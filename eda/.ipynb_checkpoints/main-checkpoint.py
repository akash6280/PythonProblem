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

"""General Proportion"""
data_pie = data.Attrition.value_counts()
plt.title("Proportion of employee data")
plt.pie(data_pie, labels=data_pie.index, autopct='%1.1f%%')
plt.show()

"""Education field"""
x = ["Low", "Medium", "High", "Very High"]
data[data['Attrition'] == 'Yes']['Education'].hist(bins=36, color='green', label="Attrition=Yes", alpha=0.6)
data[data['Attrition'] == 'No']['Education'].hist(bins=36, color='gold', label="Attrition=No", alpha=0.6)
plt.title("Education Wise distribution")
plt.xlabel("Education")
plt.legend()
x = ["Below College", "College", "Bachelor", "Master", "Doctor"]
y_pos = [1, 2, 3, 4, 5]
plt.xticks(y_pos, x)
plt.show()

"""Environment Satisfaction"""
x = ["Low", "Medium", "High", "Very High"]
plt.title('Environment Satisfaction Distribution')
plt.xlabel('Environment Satisfaction')
plt.ylabel('Number of Employees')
plt.hist(data.EnvironmentSatisfaction, label='Attrition')
y_pos = [1, 2, 3, 4]
plt.xticks(y_pos, x)
plt.show()

"""Job Involvement"""
job_involvement_data = data["JobInvolvement"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
plt.pie(data.JobInvolvement.value_counts(), labels=x, colors=colors, shadow=True, startangle=140, autopct='%1.1f%%')
plt.title("Job involvement Distribution")
plt.show()

"""Job Satisfaction"""
plt.ylabel("No of employees")
sns.countplot(x="JobSatisfaction", hue="Attrition", data=data)
plt.show()

"""Age Distribution"""
sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))
plt.title('Organization Attrition Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of person')
plt.hist([data_attr_yes.Age, data_attr_no.Age], bins=np.arange(20, 70, 5), color=['orange', 'green'], stacked=True)
plt.legend(['Attrited', 'Not Attrited'])
plt.show()

"""Overtime Factor"""
plt.ylabel("No of employees")
sns.countplot(data=data, x="OverTime", hue="Attrition")
plt.show()

"""year promotion factor"""
sns.scatterplot(data.YearsSinceLastPromotion, data['YearsSinceLastPromotion'].value_counts(), hue=data.Attrition, s=100)
plt.xlabel("YearsSinceLastPromotion")
plt.ylabel("No of Associates")
plt.show()

"""Gender wise job satisfaction"""
sns.boxplot(x=data["Gender"], y=data["JobSatisfaction"], hue=data['Attrition'], palette="Set1",
            linewidth=2.5)
plt.show()

"""Performance Rating wise job satisfaction"""
sns.barplot(y="JobSatisfaction", x="PerformanceRating", hue="Attrition", data=data)
plt.show()

