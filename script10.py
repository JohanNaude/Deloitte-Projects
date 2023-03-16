# What was the most common interaction with the android frontend component and what was the average duration of the interactions?
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

# Filter the data for android frontend component interactions
android_interactions = df[df['component'] == 'android frontend']

# Calculate the most common interaction
most_common_interaction = android_interactions['interaction'].mode()[0]

# Calculate the average duration of interactions
avg_duration = android_interactions['duration'].mean()

# Print the results
print(f"The most common interaction with the android frontend component is '{most_common_interaction}', with an average duration of {avg_duration:.2f} seconds.")