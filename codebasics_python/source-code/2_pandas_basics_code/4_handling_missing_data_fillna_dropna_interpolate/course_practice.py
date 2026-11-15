import pandas as pd
import numpy as np

df_weather = pd.read_csv("weather_data.csv", parse_dates=['day'])
# print(df_weather)

df_weather.set_index('day', inplace=True)
print(df_weather)
#fill ever wher you see na with 0
df_fill = df_weather.fillna(0)
print(df_fill)

#fill with sepcifc data base on each colum
df_fill_spec = df_weather.fillna({
    'temperature': df_weather.temperature.mean(),
    "windspeed": df_weather.windspeed.mean(),
    "event": 'no event'
})
print(f"fill with dict: {df_fill_spec}")

#forward fill, it it fill the na with a non nanpreceding value
#limit fill based on thenumber of count provided not continiously
df_fill_f = df_weather.ffill(limit=1)
print(f"fill with forward movement: \n{df_fill_f}")
#backward filling
# df_fill_b = df_weather.bfill()
# df_fill_b = df_weather.bfill(axis="columns") defalt is in row for the specific column
# print(f"fill with backward movement: \n{df_fill_b}")

#interpolate check beteen to valid value and calculate the value for the na between them
num_col = df_weather.select_dtypes(include="number").columns
df_weather[num_col] = df_weather[num_col].interpolate()
print(df_weather)

# print(df_weather.dropna())
# print(df_weather.dropna(how=all))
#thresh=2 Rule: Keep rows/columns where valid data count ≥ 2.
#Any row or column with fewer than 2 valid values (meaning 0 or 1 valid values) gets dropped.
print(df_weather.dropna(thresh=1))


