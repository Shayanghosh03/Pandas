"""
Combine the DataFrames like Vertically or Horizontally
Verticalli- Row-Wise
Horizontally- Column-Wise

pd.concate([df1, df2], axis=0, ignore_index=True)

axis=0 row wise
axis=1 column wise
"""

import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomerID':[1,2,3,4],
    'Name':['Shayan','Sumanta','Anik','Sonali']
})

df_Region2 = pd.DataFrame({
    'CustomerID':[5,6,7,8],
    'Name':['Shayam','Baburau','Amri','Tushar']
})

# Concatente Vertically
print("Concatente Vertically")
df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True)
print(df_concat)

# Concatente Horizontally
print("Concatente Hrizontally")
df_concat = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print(df_concat)