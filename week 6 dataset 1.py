import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

cars = pd.read_csv(r"D:\Somya\prepinsta internship\week 6\cars_ds_final.csv")
cars.replace("",np.NaN, inplace=True)# replacing missing values to NaN values

# dropping the entire row of missing values in Make attribute in the dataset
cars.dropna(subset=["Make"], axis=0, inplace=True)

cars["Car Name"] = cars["Make"]+ "-" + cars["Model"]
cars['Ex-Showroom_Price'] = cars['Ex-Showroom_Price'].str.replace('Rs. ','')
cars['Ex-Showroom_Price'] = cars['Ex-Showroom_Price'].str.replace(',','')
cars['Ex-Showroom_Price'] = cars['Ex-Showroom_Price'].astype(int)

print(cars.head(5))
print("")
print(cars.describe(include="all"))
print("")
print(cars["Make"].value_counts())
print("")
print(cars["Model"].value_counts())
print("")
print(cars["USB_Ports"].value_counts())
print("")
print(cars["Battery"].value_counts())

sns.displot(cars['Ex-Showroom_Price'])
plt.show()

plt.ticklabel_format(style="plain")
sns.histplot(cars["Ex-Showroom_Price"], kde=True)
plt.xlabel("Ex-showroom Price")
plt.title("Histogram Plot")
plt.axis([0,70000000,0,300])
plt.show()

sns.countplot(x="Doors", data=cars)
plt.show()