import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

daily_activity_path = r"D:\Somya\prepinsta internship\week 8\dailyActivity_merged.csv"
hourly_calories_path = r"D:\Somya\prepinsta internship\week 8\hourlyCalories_merged.csv"
hourly_intensities_path = r"D:\Somya\prepinsta internship\week 8\hourlyIntensities_merged.csv"
hourly_steps_path = r"D:\Somya\prepinsta internship\week 8\hourlySteps_merged.csv"
minute_calories_path = r"D:\Somya\prepinsta internship\week 8\minuteCaloriesNarrow_merged.csv"
minute_MET_path = r"D:\Somya\prepinsta internship\week 8\minuteMETsNarrow_merged.csv"
minute_steps_path = r"D:\Somya\prepinsta internship\week 8\minuteStepsNarrow_merged.csv"
heartrate_path = r"D:\Somya\prepinsta internship\week 8\heartrate_seconds_merged.csv"
weight_path = r"D:\Somya\prepinsta internship\week 8\weightLogInfo_merged.csv"
sleepday_payth = r"D:\Somya\prepinsta internship\week 8\sleepDay_merged.csv"

daily_data = pd.read_csv(daily_activity_path, encoding= "latin1")
hourly_calories = pd.read_csv(hourly_calories_path, encoding="latin1")
hourly_intensities = pd.read_csv(hourly_intensities_path, encoding="latin1")
hourly_steps = pd.read_csv(hourly_steps_path, encoding="latin1")
minute_calories = pd.read_csv(minute_calories_path, encoding="latin1")
minute_MET = pd.read_csv(minute_MET_path, encoding="latin1")
minute_steps = pd.read_csv(minute_steps_path, encoding="latin1")
heartrate = pd.read_csv(heartrate_path, encoding="latin1")
weight = pd.read_csv(weight_path,encoding="latin1")
sleep = pd.read_csv(sleepday_payth,encoding="latin1")

daily_data["ActivityDate"] = pd.to_datetime(daily_data["ActivityDate"])
daily_data["ActivityDate"] = daily_data["ActivityDate"].dt.strftime("%Y-%m-%d %H:%M:%S")

hourly_data1 = pd.merge(hourly_calories,hourly_intensities,how="left",on=["Id","ActivityHour"])
hourly_data = pd.merge(hourly_data1,hourly_steps,how="left",on=["Id","ActivityHour"])

minute_data1 = pd.merge(minute_calories,minute_MET,how="left",on=["Id","ActivityMinute"])
minute_data = pd.merge(minute_data1,minute_steps,how="left",on=["Id","ActivityMinute"])

weight["Date"] = pd.to_datetime(weight["Date"])
weight["Date"] = weight["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")
sleep["SleepDay"] = pd.to_datetime(sleep["SleepDay"])
sleep["SleepDay"] = sleep["SleepDay"].dt.strftime("%Y-%m-%d %H:%M:%S")

print("Daily Data: ")
print(daily_data.head(10))
print(daily_data.describe())
print(daily_data.columns)
print("")

daily_data['TotalSteps'].hist(edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Total Steps')
plt.show()

daily_data['TotalDistance'].hist(edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Total Distance')
plt.show()

daily_data['Calories'].hist(edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Calories')
plt.show()

sns.heatmap(daily_data[["TotalSteps","Calories"]].corr(), annot=True)
plt.title("correlation heatmap between total steps and calories")
plt.show()

sns.heatmap(daily_data[["TotalDistance","Calories"]].corr(), annot=True)
plt.title("correlation heatmap between total distance and calories")
plt.show()

sns.heatmap(daily_data[["VeryActiveMinutes","TotalSteps"]].corr(), annot=True)
plt.title("correlation heatmap between very active minutes and total steps")
plt.show()

sns.heatmap(daily_data[["FairlyActiveMinutes","TotalSteps"]].corr(), annot=True)
plt.title("correaltion heatmap between fairly active minute and total steps")
plt.show()

sns.heatmap(daily_data[["LightlyActiveMinutes","TotalSteps"]].corr(), annot=True)
plt.title("correlation heatmap between lightly active minute and total steps")
plt.show()

sns.heatmap(daily_data[["SedentaryMinutes","TotalSteps"]].corr(), annot=True)
plt.title("correlation heatmap between sedentary minutes and total steps")
plt.show()

print("hour data: ")
print(hourly_data.head(10))
print(hourly_data.describe())
print("")

sns.heatmap(hourly_data[["Calories","StepTotal"]].corr(), annot=True)
plt.title("correlation heatmap between calories and total steps on hourly basis")
plt.show()

sns.heatmap(hourly_data[["TotalIntensity","StepTotal"]].corr(), annot=True)
plt.title("correlation heatmap between total intensity and total steps on hourly basis")
plt.show()

print("Minute Data: ")
print(minute_data.head(5))
print(minute_data.describe())
print("")

print("heartrate data: ")
print(heartrate.head(5))
print(heartrate.describe())
print("")
plt.boxplot(heartrate["Value"])
plt.title("box plot of heart rate")
plt.show()

print("Weight Data: ")
print(weight.head(5))
print(weight.describe(include="all"))
print("")

print("Sleep Data: ")
print(sleep.head(5))
print(sleep.describe())
plt.boxplot(sleep[["TotalSleepRecords","TotalMinutesAsleep","TotalTimeInBed"]], labels=["TotalSleepRecords","TotalMinutesAsleep","TotalTimeInBed"])
plt.title("box plot of sleep schedule")
plt.show()

