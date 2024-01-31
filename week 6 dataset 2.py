import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

dataframe = pd.read_csv(r"D:\Somya\prepinsta internship\week 6\train.csv")

dataframe["Order Date"] = pd.to_datetime(dataframe["Order Date"], format="%d-%m-%Y")
dataframe["Ship Date"] = pd.to_datetime(dataframe["Ship Date"], format="%d-%m-%Y")
dataframe["Order Year"] = dataframe["Order Date"].dt.year
dataframe["Ship Year"] = dataframe["Ship Date"].dt.year

print(dataframe.head(5))
print("")
print(dataframe.shape)
print("")
print(dataframe.describe(include="all"))
print("")
print(dataframe["Order Year"].value_counts())
print("")
print(dataframe["Ship Year"].value_counts())
print("")
print(dataframe["Ship Mode"].value_counts())
print("")
print(dataframe["Category"].value_counts())
print("")
print(dataframe["State"].value_counts())
print("")
print(dataframe["Segment"].value_counts())
print("")

sns.countplot(x="Ship Mode", data=dataframe)
plt.xlabel("Ship Mode")
plt.ylabel("count")
plt.title("bar chart for ship mode")
plt.show()

sns.countplot(x="Order Year", data=dataframe)
plt.xlabel("Order Year")
plt.ylabel("count")
plt.title("bar chart for order year")
plt.show()

sns.countplot(x="Ship Year", data=dataframe)
plt.xlabel("Ship Year")
plt.ylabel("count")
plt.title("bar chart for ship year")
plt.show()

sns.countplot(x="State", data=dataframe)
plt.xlabel("State")
plt.ylabel("count")
plt.title("bar chart showing number of orders in each state")
plt.show()

cross_tab = pd.crosstab(dataframe["Order Year"], dataframe["Ship Mode"])
sns.heatmap(cross_tab, annot=True, cmap='viridis')
plt.xlabel("Order Year")
plt.ylabel("Ship Mode")
plt.title("showing the relation between order year and ship mode")
plt.show()

cross_tab = pd.crosstab(dataframe["Segment"], dataframe["Ship Mode"])
sns.heatmap(cross_tab, annot=True, cmap='viridis')
plt.xlabel("Segment")
plt.ylabel("Ship Mode")
plt.title("showing the relation between segment and ship mode")
plt.show()

cross_tab = pd.crosstab(dataframe["Segment"], dataframe["Category"])
sns.heatmap(cross_tab, annot=True, cmap='viridis')
plt.xlabel("Segment")
plt.ylabel("Category")
plt.title("showing the relation between segment and category ordered")
plt.show()


