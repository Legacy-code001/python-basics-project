import pandas as pd

df = pd.read_csv("bengaluru_house_prices.csv")
print(df.head(4))

df_unique = df['area_type'].unique()
df_column = df[df.area_type].columns
#filter the data
df[(df['size'] == '2 BHK') & (df['area_type'] == 'Super built-up  Area')]

#Add the column 'price_category'
df['price_category'] = df.apply(lambda x: "Affordable" if x['price'] < 80 else "High Cost", axis=1)

#write condition here
df[df['price'] > df['price'].mean()]

# print(df_column)
print(df_unique)
print(df.head())