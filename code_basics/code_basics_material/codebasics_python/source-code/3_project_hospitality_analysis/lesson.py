import pandas as pd
import numpy as np

df_fact_bookings = pd.read_csv("datasets/fact_bookings.csv")
print(f"display booking sample \n {df_fact_bookings.head()}")
print(f"the co ordinate: {df_fact_bookings.shape}")
print(f"num of guest less/zero {df_fact_bookings[df_fact_bookings['no_guests'] <= 0]}")
print(f"column identified: {df_fact_bookings.columns}")
print(f"avilable room category: \n {df_fact_bookings.room_category.unique()}")
print(f"avilable booking platform: \n {df_fact_bookings.booking_platform.unique()}")
print(f"avilable booking status: \n {df_fact_bookings.booking_status.unique()}")
print(f"avilable room category: \n {df_fact_bookings.booking_status.value_counts()}")
print(f"avilable room category: \n {df_fact_bookings.booking_platform.value_counts().plot(kind="bar")}")
print(f"avilable room category: \n {df_fact_bookings.booking_status.describe()}")
print(f"avilable room category: \n {df_fact_bookings.describe()}")


df_fact_agg_bookings = pd.read_csv("datasets/fact_aggregated_bookings.csv")
print(f"aggregated bookings: {df_fact_agg_bookings.head(5)}")
print(f"aggregated unique bookings: {df_fact_agg_bookings.property_id.unique()}")
print(f"aggregated value_counts bookings: {df_fact_agg_bookings.property_id.value_counts()}")

print(f"aggregated unique capaccity: {df_fact_agg_bookings.capacity.unique()}")
print(f"aggregated unique bookings: {df_fact_agg_bookings[df_fact_agg_bookings.successful_bookings > df_fact_agg_bookings.capacity] }")

df_greater_successful = df_fact_agg_bookings[df_fact_agg_bookings.successful_bookings > df_fact_agg_bookings.capacity]

print(f"succesful booking greater than capacity: \n {df_greater_successful.check_in_date}")

print(f"highest capacity: {df_greater_successful["capacity"].max()}")

print(f"Booking per property: {df_fact_agg_bookings.groupby("property_id")["successful_bookings"].sum()}")

# print(f"group by property: {df_fact_agg_bookings.groupby("property_id")}")

# print(f"number of individual succesful_bookings: {df_fact_agg_bookings.successful_bookings.value_counts()}")

"""DATA CLEANING"""
print(f"display booking sample \n {df_fact_bookings.head(4)}")
print(f"display booking columns \n {df_fact_bookings.columns}")
print(f"display booking describe \n {df_fact_bookings.describe()}")
print(f"invalid guest: \n {df_fact_bookings[df_fact_bookings.no_guests <= 0]}")

# df_fact_bookings = df_fact_bookings[df_fact_bookings.no_guests <= 0]

# outliers removed in revenues genrated (avg > 3 + std)
min, max = df_fact_bookings.revenue_generated.min(), df_fact_bookings.revenue_generated.max()
print(min, max)
higher_limit = df_fact_bookings.revenue_generated.mean() + 3*df_fact_bookings.revenue_generated.std()

df_fact_bookings = df_fact_bookings[df_fact_bookings.revenue_generated <= higher_limit ]

print(f"after outlier is removed: {df_fact_bookings}")

# for revenue_realized 
higher_limit_realized = df_fact_bookings.revenue_realized.mean() + 3*df_fact_bookings.revenue_realized.std()

df_fact_bookings[df_fact_bookings.revenue_realized <= higher_limit_realized]

print(f"after outlier is removed: {df_fact_bookings}")

print(f"chcking for the counts: {df_fact_bookings[df_fact_bookings.revenue_realized > higher_limit_realized]}")

print(df_fact_bookings[df_fact_bookings.room_category=="RT4"].revenue_realized.describe())

higher_fact_bookings = df_fact_bookings[df_fact_bookings.revenue_realized > higher_limit_realized]

# print(higher_fact_bookings.room_category) all RT4


# counting isnull
# Total values in our dataframe is 134576. Out of that 77899 rows has null rating. Since there are many rows with null rating, we should not filter these values. Also we should not replace this rating with a median or mean rating etc 
print(f"counting the num of num: {df_fact_bookings.isnull().sum()}") 
print(df_fact_agg_bookings)

df_fact_agg_bookings["acc_pcc"] = df_fact_agg_bookings["successful_bookings"]/df_fact_agg_bookings["capacity"]
df_fact_agg_bookings["acc_pcc"] = df_fact_agg_bookings["acc_pcc"].apply(lambda x: round(x * 100, 2))
print(df_fact_agg_bookings)

# ?printing avg occ_rate per city
# when occupancy is better
# occupancy for diffrent city in the month if june
# add data from august