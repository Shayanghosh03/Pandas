# Sorting data
# Sorting data 1 column sort_value()
# df.sort_values(by="Column Name", True/False, inplace = True)
import pandas as pd

data= {
    "Name":["Arun","Barun","Karun"],
    "Age":[28,34,32],
    "Salary":[10000,20000,30000]
}

df=pd.DataFrame(data)
df.sort_values(by="Age", ascending = False, inplace = True)
print("Sorted Age by Descending..")
print(df)