### Task 1: Client Sales Data

# **Scenario:**  One of the Python developers, who was handling a retail client, went on vacation. However, the client has an urgent requirement to understand their sales data. Loki reached out to you for help with this. The sales records are stored in JSON format, detailing products, quantities sold, and sales categories.


# 1. Load sales data from ```sales_data.json``` into a dictionary.

   
# This task helps you provide actionable business insights from raw sales data.

import json

with open("sales_data.json") as data:
    sales_dict = json.load(data)
    print(sales_dict)

# ### Task 2: Calculate and Display Total Sales by Category

# **Scenario:** Continuing your role, after successfully loading and organizing the sales data from a retail client, your next step is to provide a breakdown of total sales per category.

# 1. Aggregate this data by product category to calculate total sales per category.
# 2. Print the results, showing the total sales for each product category.


def calCategory():
    electronic = 0
    apparel = 0
    home_appliances = 0
    for val in sales_dict:
        if val['category'] == "Electronics":
            total = val['price_per_unit'] * val['quantity']
            electronic += total
        if val['category'] == "Apparel":
            total = val['price_per_unit'] * val['quantity']
            apparel += total
        if val['category'] == "Home Appliances":
            total = val['price_per_unit'] * val['quantity']
            home_appliances += total
    return (f"electronics {electronic} apparel {apparel} home_appliances {home_appliances}")

print(calCategory())

calCategory_str = calCategory()
arr_calCategory = calCategory_str.split(" ")
print(arr_calCategory)

total_price = [int(arr_calCategory[x]) for x in range(len(arr_calCategory) + 1) if x > 0 and x % 2 != 0]
print(total_price)

category = [arr_calCategory[x] for x in range(len(arr_calCategory)) if x == 0 or  x % 2 == 0]

# print(category)
# print(total_price)



def sales_dict():
    sales_category = []

    for cat in range(len(category)):
        val = {
            "category": category[cat],
            "total_price": total_price[cat]
        }
        
        sales_category.append(val)
    return sales_category
print(sales_dict())

sales_dict_list = sales_dict()

with open("aggregated_sales.json", "w") as f:
    json.dump(sales_dict_list, f, indent=4)



    

