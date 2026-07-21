# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal


# city = input("what is your city: ")


# if city in ["mumbai", "banglore", "chennai", "delhi"]:
#     print("The city is in india")
# elif city in ["lahore","karachi","islamabad"]:
#     print("the city is in pakistan")
# else:
#     print("The city is in bangladesh")

# check_city_1 = input("enter the first check: ")
# check_city_2 = input("enter the second check: ")

# if check_city_1 and check_city_2 in ["mumbai", "banglore", "chennai", "delhi"]:
#     print("both city are in india")
# elif check_city_1 and check_city_2 in ["lahore","karachi","islamabad"]:
#     print("both city are in pakistan")
# elif check_city_1 and check_city_1 in  ["dhaka", "khulna", "rangpur"]:
#     print("both city are in bangladesh")
# else:
#     print("they dont belong to the same country")

"""2"""

level_sugar = input("enter your fsting level sugar: ")

if int(level_sugar) < 80:
    print("sugar level is low")
elif int(level_sugar) > 100:
    print("sugar level is high")
elif int(level_sugar) >= 80 and int(level_sugar) <= 100:
    print("sugar level is normal")