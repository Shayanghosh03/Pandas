import pandas as pd

data = {
    "Name":['Shayan','Sumanta','Sonali','Arnab','Rohit','Raj','Simran','Ankit'],
    "Age":[10,23,45,67,89,56,78,34],
    "Salary":[5000,7000,4500,8900,10000,23000,6700,5500],
    "Performane Score":[89,90,66,99,78,92,99,88]
}

df = pd.DataFrame(data)
print("Sample DataFrame")
print(df)

# Select sinle column
print("Names (Single column return series)")
# print(df["Name"])
name = df["Name"]
print(name)

# Selecting Multiple columns
subset = df[["Name","Age"]]
print("\n Subset with name with age")
print(subset)
