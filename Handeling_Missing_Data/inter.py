import pandas as pd

data = {
    "Name":['Shayan','Sumanta','Sonali','Arnab','Rohit','Raj','Simran','Ankit'],
    "Age":[10,None,45,67,89,56,78,34],
    "Salary":[5000,None,4500,8900,10000,23000,6700,5500],
    "Performane Score":[89,None,66,99,78,92,99,88]
}

df=pd.DataFrame(data)
print(df)

# Linear, polynomial, time
df.interpolate(method="linear", axis=0, inplace=True)
