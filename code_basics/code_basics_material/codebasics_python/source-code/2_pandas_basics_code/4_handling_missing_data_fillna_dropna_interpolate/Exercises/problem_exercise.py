import pandas as pd
import numpy as np

#### <font color="purple">**Question1**</font>
# - Read the csv file 'fruits_data.csv' into the dataframe 'df'.
# - show the number of rows and columns in it.
# - list all the columns present in the dataframe.
# - show the dataframe

df = pd.read_csv("fruits_data.csv")

row, col = df.shape
print(f"row: {row} and col: {col}" )
print(df.columns)
print(df)

#fill null values with -1 and store it to 'new_df'
new_df = df.fillna(-1)

#show the dataframe 'new_df'
print(new_df)

### <font color="purple">**Question3**</font>
# Fill the null values in respective columns like below:

#     - apple(1kg): Mean value of that column
#     - banana(1 dozen): Mean value of that column
#     - grapes(1kg): Median value of that column
#     - mango(1kg): Median value of that column
#     - Water Melons(1): Fill null values with "Not Available".
    
# Finally store the output to 'new_df' variable

#write the code to fill null values as per above condition
#store the result to 'new_df' variable
new_df2 = df.fillna({
    "apple(1kg)": df["apple(1kg)"].mean(),
    "banana(1 dozen)": df["banana(1 dozen)"].mean(),
    "grapes(1kg)": df["grapes(1kg)"].median(),
    "mango(1kg)": df["mango(1kg)"].median(),
    "Melons(1)": "Not Available",
})


#show the dataframe 'new_df'
print(new_df2)

### <font color="purple">**Question4**</font>

# - Fill the null values with the non-null value before it (Forward fill method)
# - Store the result in 'new_df'.
#fill null values using 'ffill'
new_df3 = df.ffill()


#show the dataframe 'new_df'
print(new_df3)

### <font color="purple">**Question5**</font>
# - Drop the rows if it does not contain atleast 4 non-null values (use the concept of thresholding).
# - store the result in 'new_df'
new_df4 = df.dropna(thresh=4)
print(new_df4)


### <font color="purple">**Question6**</font>


# - Finally, remove the row if it contain null value and store the result in 'new_df'
# - save that dataframe to csv:'final_data.csv' and make sure to set index to False

#write the code here
new_df5 = df.dropna(how="any")
print(new_df5)


#show the dataframe 'new_df'
new_df5.to_csv("new_df5.csv", index=False)