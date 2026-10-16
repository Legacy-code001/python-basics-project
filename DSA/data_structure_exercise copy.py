# Exercise: Hash Table: New York City Weather Analysis
# (1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

#   (a) What was the average temperature in first week of Jan

#   (b) What was the maximum temperature in first 10 days of Jan

#   Figure out data structure that is best for this problem

import json

array = [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]

# book = {}

arr = []
# arr_int = []
weather_dict = {}
arr_temp = []
# s = json.dumps(book)
# print(s)

# with open(r"C:\Users\owner\Desktop\book.csv", "w") as f:
#     f.write(s)

with open(r"C:\Users\owner\Desktop\book.csv", "r") as f:
    s = f.read()
    print(s)
    print(type(s))

    # for line in s:
    token = s.split("\n")
    for i, e in enumerate(token):
        new = e.split(",")
        # print(new)
        arr.append(new)
    print(arr)

    for i, e in enumerate(arr):
            day = e[0]
            print(day)
            try:
                temp = int(e[1])
                arr_temp.append(temp)
                print(temp)
                weather_dict[day] = temp
            except:
                print("invalid")

total = 0
count = 0
# for i, e in enumerate(arr_temp):
#     print(i, e)
#     if i < 5:
#         total += e
while count < len(arr_temp) - 1:
    total += arr_temp[count]
    count+=1
print(total)
print(weather_dict)
print(arr_temp)
print(weather_dict["Jan-04"])
# print(arr)
# sum_of_five = sum(arr[0:4])
# avg_of_five = sum_of_five/len(arr[0:4])
# print(len(arr[0:4]))
# print(avg_of_five)
# print(max(arr[:4]))

