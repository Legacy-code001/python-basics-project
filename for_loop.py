# After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

# Print square of all numbers between 1 to 10 except even numbers
# Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
# Write a program that prints following shape

# count = 0
# for i,v in enumerate(result):
#     if v == "heads":
#         count += 1
# print(count)

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i ** 2)
#     else:
#         print(i)


# month_list = ["jan", "feb", "mar", "april", "may"]
# expenses_amount = input("the expenses amount is: ")
# expenses_amount = int(expenses_amount)
# month = -1

# for i in range(len(expense_list)):
#     if  expenses_amount == expense_list[i]:
#         month = i
#         break
    
# if month != -1:
#         print(f"you spent {expenses_amount} in month of {month_list[month]}")

# if month == -1:
#          print(f"you did not spent {expenses_amount} in any month")
    
# for i,v in enumerate(expense_list):
#     if v == int(expenses_amount):
#         month_num = i
#     for i, val in enumerate(month):
#         if month_num == i:
#             print(val)
#     else:
#         print("amount is not available")


avilable_km = [1,2,3,4,5]
# # decision = input("are you tired?: ")

# for i in range(len(avilable_km)):
#         decision = input("are you tired?: ")
#         if decision == "yes":
#                 print("you did not finish the race")
#                 break
#         if decision == "no" and  avilable_km[i] != avilable_km[-1]:
#                 print("are you tired")
#                 continue
#         if avilable_km[i] == avilable_km[-1]:
#                 print("congratulation")

s = ' '
for i in range(len(avilable_km)):
        s += '*'
        print(s)


        