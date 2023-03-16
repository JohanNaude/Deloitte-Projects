# What was the average duration for interactions with the web frontend component and were there any instances of downtime?
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

import numpy as np

# Get the subset of data for the web frontend component
web_frontend_data = df[df['component'] == 'web frontend']

# Compute the average duration of interactions
average_duration = np.mean(web_frontend_data['duration'])

# Check if there were any instances of downtime
downtime = web_frontend_data['downtime'].sum() 

if downtime > 0:
    print(f"The average duration for interactions with the web frontend component is {average_duration:.2f} seconds and there were {downtime:.2f} seconds of downtime.")
else:
    print(f"The average duration for interactions with the web frontend component is {average_duration:.2f} seconds and there were no instances of downtime.")
