# I imported the data to put it into a dataframe and then represent it in charts
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")


# filter the data based on the specified criteria
filtered_data = df[(df["component"] == "android frontend") & (df["interaction"] == "bounce")]

# check if there were any bounce interactions
if filtered_data.empty:
    print("There were no bounce interactions with the android frontend component.")
else:
    # calculate the total duration of the bounce interactions
    total_duration = filtered_data["duration"].sum()
    print("There were {} bounce interactions with the android frontend component, and their total duration was {} seconds.".format(len(filtered_data), total_duration))