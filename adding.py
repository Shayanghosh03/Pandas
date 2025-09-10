import pandas as pd

data = {
    "Name":['Shayan','Sumanta','Sonali','Arnab','Rohit','Raj','Simran','Ankit'],
    "Age":[10,23,45,67,89,56,78,34],
    "Salary":[5000,7000,4500,8900,10000,23000,6700,5500],
    "Performane Score":[89,90,66,99,78,92,99,88]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

df.insert(0,"Employee ID",[101,201,303,406,708,809,790,450])
print(df)