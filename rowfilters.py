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

high_salary = df[df['Salary']>10000]
print("Empoyee with salary > 10000")
print(high_salary)

# Filtering salary > 10000 & cchaage >30

filtered = df[(df['Age']>30) & (df['Salary']>10000)]
print("Employ with salary > 10000 and age >30")
print(filtered)


filtered_or = df[(df["Age"]>30) | (df["Performane Score"]>95)]
print(filtered_or)