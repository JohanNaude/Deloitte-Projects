# What were the interactions and duration with the django controller component and what were the HTTP responses.
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

# filter the dataframe to only include rows with the django controller component
df_django = df[df['component'] == 'django controller']

# select only the 'interaction', 'duration', and 'downtime' columns
df_django = df_django[['interaction', 'duration', 'downtime']]

# filter the dataframe to only include rows with HTTP response codes
df_http = df_django[df_django['interaction'].str.startswith('HTTP')]

# print the resulting dataframe
print(df_http)