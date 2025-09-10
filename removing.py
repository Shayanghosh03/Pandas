import pandas as pd

data = {
    "Name":['Shayan','Sumanta','Sonali','Arnab','Rohit','Raj','Simran','Ankit'],
    "Age":[10,23,45,67,89,56,78,34],
    "Salary":[5000,7000,4500,8900,10000,23000,6700,5500],
    "Performane Score":[89,90,66,99,78,92,99,88]
}

df = pd.DataFrame(data)
print(df)

#df.drop(columns = ["columnName"], inplace=True)

# print("Modify Data")
# df.drop(columns = ["Performane Score"], inplace=True) 
# print(df)

print("Modify Data")
df.drop(columns = ["Performane Score", "Age"], inplace=True) 
print(df)
