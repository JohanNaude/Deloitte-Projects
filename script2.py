# Were there any server errors in the sap shipping management system component and how long was the downtime for each error?
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

# Filter for server errors in the sap shipping management system component
sap_errors = df[(df['component'] == 'sap shipping management system') & (df['interaction'] == 'server error')]

# Extract the relevant columns (date, duration, downtime) and display the results
sap_error_downtime = sap_errors[['date', 'duration', 'downtime']]
print(sap_error_downtime)