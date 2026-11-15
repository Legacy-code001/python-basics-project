import pandas as pd
import numpy as np


# # df = pd.read_csv("stock_data.csv", header=1)
# df = pd.read_csv("stock_data.csv", skiprows=1)
# #REPLACING EITHER ONE OR HEADER NAME
# # df = pd.read_csv("stock_data.csv", skiprows=1, names=["stock_symbol","eps","revenue","price","personality"])
# #PRINTING OUT NUMBER OF ROWS SPECIFY JUST LIKE head(3)
# # df = pd.read_csv("stock_data.csv", skiprows=1, nrows=3)
# df = pd.read_csv("stock_data.csv", skiprows=1, na_values={
#     'eps': "not available",
#     'revenue': [-1],
#     'people': ['not available', 'n.a.'],
#     'price': "n.a."
# })
# #replace every "n.a", "not available" with NaN  
# # df = pd.read_csv("stock_data.csv", skiprows=1, na_values=["n.a", "not available"])

# def safe_divide(x,y):
#     if pd.isna(x) or pd.isna(y):
#         return np.nan
#     return np.divide(float(x),float(y))
    
# #pd.isna() function in pandas checks for missing values in your data, returning True for missing entries (NaN, None, or NaT) and False for valid data
# df["pe"] = df.apply(lambda x: safe_divide(x['price'], x['eps']), axis=1)

# #axis=1 tells pandas to apply the function horizontally across each row rather than vertically down each column.
# # df = df.head()

# #df.to_csv("pe_my.csv", index=False)
# #df.to_csv("pe_my1.csv", header=False)
# df.to_csv("pe_my2.csv", columns=["tickers","price"], index=False)
# # print(df)

# df_movies = pd.read_excel("movies_db.xlsx", "movies")
# df_financials = pd.read_excel("movies_db.xlsx", "financials")
# df_financials_5 = df_financials.head(5)
# # print(df_financials_5)
# df_2_5 = df_movies.head(5)

# def same_currency(curr):
#     if curr == "$$" or curr == "Dollars":
#         return "USD"
#     return curr

# df_financials_5_curr = pd.read_excel("movies_db.xlsx", "financials", converters={
#     'currency': same_currency
# })
# print(df_financials_5_curr)
# #pd to merge directly
# df_merged = pd.merge(df_movies, df_financials, on="movie_id")
# print(df_merged.head(5))
# print(df_2_5)

# #creatinf excel file
# df_merged.to_excel("merged.xlsx", sheet_name="mergred", index=False)

# #creating a dataframe
# first_df = pd.DataFrame({
#     "Math": [78,98,87,89],
#     "Phys": [79,90,87,85],
#     "Chm": [89,67,79,95]
# })

# Second_df = pd.DataFrame({
#     "Math": [98,88,87,79],
#     "Phys": [98, 92,89,95],
#     "Chm": [79,87,79,98]
# })

# first_df.to_excel("senior.xlsx", sheet_name="senior" )
# Second_df.to_excel("junior.xlsx", sheet_name="Junior" )

# ### <font color="purple">**Question2**</font>
# # - Add a new column "year_classify" to the above dataframe.
# # - If release_year is less than 2000, then 'before 2000' or else 'From 2000'

df_movies_data = pd.read_csv("movies_data.csv", nrows=5)
# print(df_movies_data)

print(df_movies_data.release_year)

def classifier(year):
    return 'before 2000' if year < 2000 else 'after 2000'
df_movies_data['year-classify'] = df_movies_data['release_year'].apply(lambda x: classifier(x))
print(df_movies_data)
print(df_movies_data.budget)
df_movies_data.to_csv("final_movies_data.csv", index=False)