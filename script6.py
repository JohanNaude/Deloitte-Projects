# I imported the data to put it into a dataframe and then represent it in charts
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

# Filter the dataframe to get rows where Component is 'ai engine'
ai_engine_df = df[df['component'] == 'ai engine']

# Get the downtime for the ai engine component
ai_engine_downtime = ai_engine_df['downtime'].sum()

# Get the error with the training data for the ai engine component
ai_engine_training_error = ai_engine_df[ai_engine_df['interaction'] == 'training data error']['interaction'].count()

# Print the results
print(f"The downtime for the ai engine component was {ai_engine_downtime} seconds.")
print(f"The ai engine component had {ai_engine_training_error} training data errors.")