import pandas as pd
# pd.merge(df1, df2, on="Column_Nmae", how="type of join")

# Customer DataFrames
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3,4],
    'Name':['Ramesh','Suresh','Kalpesh','Shayan']
})

# Order DataFrame

df_orders = pd.DataFrame({
    'CustomerID':[1,2,3,5],
    'OrderAmount':[250,450,550,660]
})

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
print('Inner join')
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print('Outer join')
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
print('Left join')
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print('Right join')
print(df_merged)


"""
1df = m rows
2df = n rows
m * n rows
"""
