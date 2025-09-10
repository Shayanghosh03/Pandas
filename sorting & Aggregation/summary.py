"""
df["Column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()
"""

import pandas as pd

data= {
    "Name":["Arun","Barun","Karun"],
    "Age":[28,34,32],
    "Salary":[40000,20000,30000]
}

df=pd.DataFrame(data)
print(df)

avg_salary = df['Salary'].mean()
print(avg_salary)