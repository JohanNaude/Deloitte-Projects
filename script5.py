# Were there any potential SSH threats to the shipping database component and how long was the downtime?
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

# filter the rows where the component is "shipping database" and the interaction is "potential SSH threat"
filtered_data = df[(df['component'] == 'shipping database') & (df['interaction'] == 'potential SSH threat')]

# check if there were any potential SSH threats to the shipping database component
if not filtered_data.empty:
    # get the downtime for the relevant rows
    downtime = filtered_data['downtime'].sum()
    print(f"There were potential SSH threats to the shipping database component and the total downtime was {downtime} seconds.")
else:
    print("There were no potential SSH threats to the shipping database component.")
