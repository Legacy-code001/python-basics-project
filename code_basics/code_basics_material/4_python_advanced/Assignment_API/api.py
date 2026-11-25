import requests
# The Open Brewery DB API offers detailed data on various breweries across the United States. 

# --

# ### Task 1: Fetch Brewery Data for Non-alcoholic Drink manufacturer - US client

# **Scenario:**

# As Tony Sharma mentioned during the call, he needs details about all the breweries in a specific state.

# Your task is to use the Open Brewery DB API to fetch and display brewery details based on a given state, which will be helpful for his client call tomorrow.

# **Write a Python program that:**

# 1. Uses the `requests` library to call the Open Brewery DB API to fetch brewery data based on a given state.
# 2. Parses the JSON response.
# 3. Extracts and displays the name, type, and location (city) of each brewery.
# 4. Handles errors gracefully (e.g., network issues or invalid API requests).

# Example URL for Texas Breweries: `https://api.openbrewerydb.org/v1/breweries?by_state=texas`

url = "https://api.openbrewerydb.org/v1/breweries?by_state=texas"

response = requests.get(url)

if response.status_code == 200:
    datas = response.json()
    for data in datas:
        print(f"name: {data["name"]}  type: {data["brewery_type"]} location {data["country"]}")
else:
    print("invalid data request")

url_user = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url_user)
if response.status_code == 200:
    data_values = response.json()
    for data in data_values:
        data_result = {
            "name": data["name"],
            "email": data["email"],
            "address": data["address"]
        }
    print(data_result)