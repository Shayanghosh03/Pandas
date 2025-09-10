import pandas as pd
df = pd.read_json("sample_Data.json")

print("1st 10 Rows are")
print(df.head())

print("Last 10 rows are")
print(df.tail())