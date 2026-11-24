import requests

'''fetching/geting request'''

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
# print(dir(response))
print(f"Response code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"return first data: {data[0]}")
else:
    print("failed to retrieve data")


data = {
    "title": "the title",
    "body": "the body",
    "userId": "1"
}

''' for post reqest'''
response = requests.post(url, json=data)

if response.status_code == 201:
    created_data = response.json()
    print(f"created data {created_data}")
else:
    print("no data")


#### Common Status Codes
"""
1. 200: OK (The request was successful).
1. 201: Created (The resource was successfully created).
1. 400: Bad Request (The server could not understand the request).
1. 401: Unauthorized (Authentication is required).
1. 404: Not Found (The requested resource could not be found).
1. 500: Internal Server Error (The server encountered an error)."""

url1 = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url1)

if response.status_code == 200:
    data = response.json()
    print(f"successful request with code: {response.status_code}")
elif response.status_code == 404:
    print(f"request not found with code{response.status_code}")
else:
    print(f"bad request with code: {response.status_code}")


params = {
    "userId": 1
}
response = requests.post(url, params=params)

if response.status_code == 201:
    data = response.json()
    print(f"the data by param: {data}")
else:
    print("failed to retrieve data")

# URL of the API endpoint
# url_coin = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Sending a GET request
# response = requests.get(url_coin)

# Checking the status code of the response
# try:

#     if response.status_code == 200:
#         data = response.json()
#         print("Bitcoin Price Index (BPI):")
#         print(f"USD: {data['bpi']['USD']['rate']} USD")
#         print(f"GBP: {data['bpi']['GBP']['rate']} GBP")
#         print(f"EUR: {data['bpi']['EUR']['rate']} EUR")
#     else:
#         print("Failed to retrieve data")
# except exception as e:
#     print(e)


"""open currency exchange"""
# my_app_id = b3b7b57d32ba4e709d2fc59a973a78d3
url_exchange = "https://openexchangerates.org/api/latest.json?app_id=b3b7b57d32ba4e709d2fc59a973a78d3"


response = requests.get(url_exchange)

if response.status_code == 200:
    data = response.json()
    print(data["rates"]["AED"])

