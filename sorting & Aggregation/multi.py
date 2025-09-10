import pandas as pd

data= {
    "Name":["Arun","Barun","Karun","Narun","Marun"],
    "Age":[55,34,32,55,32],
    "Salary":[40400,35000,65000,55000,67800]
}

df = pd.DataFrame(data)
print(df)
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
