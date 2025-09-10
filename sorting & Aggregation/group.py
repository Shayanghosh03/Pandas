import pandas as pd

data= {
    "Name":["Arun","Barun","Karun","Narun","Marun"],
    "Age":[28,34,32,55,28],
    "Salary":[40400,35000,65000,55000,67800]
}

df = pd.DataFrame(data)
print(df)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
