# Was there any downtime in the customer database component and what was the reason for the downtime? Give me three reasons
import pandas as pd

# read CSV data into a pandas DataFrame
df = pd.read_csv("measure.csv")

# Filter for the customer database component
customer_db = df[df['component'] == 'customer database']

# Check if there was any downtime and get the reasons for downtime
if customer_db['downtime'].sum() > 0:
    top_reasons = customer_db.groupby('interaction')['downtime'].sum().sort_values(ascending=False).head(3)
    print("The top reasons for downtime in the customer database component are:")
    for i, (interaction, downtime) in enumerate(top_reasons.items()):
        print(f"{i+1}. {interaction}: {downtime} seconds")
else:
    print("There was no downtime in the customer database component.")