import pandas as pd 
import numpy as np 


df = pd.read_csv("weather_by_cities.csv")
# print(df.head)

group_obj = df.groupby('city')
print(group_obj)
for city, details in group_obj:
    print(f"city: {city} \n details: \n {details}")

group_details = group_obj.describe()
#this give us acces to menthod we can get ro the grop data
print(group_details)

print(group_obj.max())
print(group_obj.quantile(0.75, numeric_only=True))
print (group_obj.std(numeric_only=True))
print(group_obj.count())

def grouping(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return "80-90"
    elif 40 <= df[col].loc[idx] <= 50:
        return "40-50"
    else:
        return "others"
temp_group = df.groupby(lambda idx: grouping(df, idx, "temperature" ))
for temp_range, details in temp_group:
    print(f"temp-range: \n {temp_range} \n details: {details}")
    
