import pandas as pd
data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df = pd.DataFrame(data)
print("Before Interpolation")
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print("After Interpolate")
print(df)

'''
1- time series data
2- numeric data with trends
3- avoid droping row
'''