import pandas as pd

data= {
    "Name":["Arun","Barun","Karun"],
    "Age":[28,34,32],
    "Salary":[40000,20000,30000]
}

df=pd.DataFrame(data)

df.sort_values(by=["Age", "Salary"], ascending = [True, False], inplace = True)
print("Sorted Age by Descending..")
print(df)