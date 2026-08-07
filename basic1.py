var = "welcome to python"
name = "i am abdulmueez"
# print(var)
# print(var[:7])
# print(var[8:])
# print(var.upper())
# print(var.count("o"))
# print(var.find("o"))
# print(var[::-1])
# print(var[:])
# print(var[::2])

items = {"teeth": "brush", "body": "soap", "leg": "shoe"}


# result = var + ", " + name
# result2 = '{} , {}'.format(var, name)
# result3 = 'the needs of body parts such as {0[0]}, {1[1]} and {2[1]}'.format(items)
# print(3 // 2)

# list, tuple, set, dictionary

profession = ["doctor", "engineer", "lawyer", "accountant", "pilot"]
ages = [97, 25, 77, 50]
coder = ["developer", "banker"]
# print(len(profession))

# print(profession + coder)

# print("MLOPs" in profession)

# print(agse[0] + 1)
# print(ages)

# for age in ages:
#     print(age)

# div = ages[1] / 2
# print(round(div))

div = ages[1] / 2
# print((div))
# print(round(div, 2))

val1 = 26
val2 = "3"
# print(val1/int(val2))
# print (str(val1) + val2)

# profession.append("geologist")
# profession.insert(3, "pharmacist")
# profession.extend(coder)
# profession.remove("banker")
# remVal = profession.pop()
# print(remVal)
# profession.reverse()
# # profession.sort()
# ages.sort()
profession.sort(reverse=True)
# print(profession)
# print(profession.index("doctor"))
# print(profession)
# functions min, max, sum
# print(sum(ages))

for index, career in enumerate(profession, start=1): 
    print(index, career)

joined_coder = ' - '.join(coder)
# print(coder)
# print(joined_coder)

# print(joined_coder.split(" - "))

# tuple
var_tuple = ("laptop", "phone", "monitor")
var_tuple_2 = var_tuple

# print(var_tuple_2)

# tuple does not support  mutation
# var_tuple[1] = "samsung"
# print(var_tuple_2)
# print(var_tuple)

# set - random disply of values, it also dont acomodate duplicate, 
# union, interection, 

var_set = {'math',' chem',' bio','eng',}
var_set_Art = {"lit", "civic", "math", "eng"}
var_set_2 = var_set
# print(var_set)
# print(var_set_2)
# print(var_set.union(var_set_Art))
# print(var_set.intersection(var_set_Art))
# print(var_set.difference(var_set_Art))


val = []
val2 = ()
val3 = set()
val.append("habeeb")
val.append("mueez")
val.insert(1, "malik")
# print(val2)
val.reverse()
# print(val)
val2 = tuple(val)
val3 = set(val)
# print(val2)
# print(val3)
# print(len(val))


# dictionary

first_dic = {"car": "drive", "bike": "ride", "plane": "fly", "boat": "sail"}

# for i in first_dic:
#     print(i)

# for i, val in first_dic.items():
#     print(i, val)

# (print(first_dic['car']))

# better written as this

# print(first_dic.get('boat', "not avilable"))


<<<<<<< HEAD
=======
# drint = {"coke", "fanta", "pepsi"}
# # drint.add("mint")
# drint.update("mint")
# print(drint)


>>>>>>> 0d57839 (first-aug)
# print(first_dic.pop("boat"))
# first_dic.update({"boat": "sail", "plane": "flies"})
# print(first_dic)
# print(first_dic.values())
# print(first_dic.keys())
# print(len(first_dic))

#  conditional and boolean or boolean
school = ""
val = False
val3 = "false"
val4 = 4
val5 = 34

# not for negation
# if not school:
#     print("my alma mata")
# else:
#     print("advance secondary school")

# if school and val:
#     print("great")
# elif school:
#     print("good")
# else:
#     print("bad")

# or boolean operator either to be true
# and both to occur for the condition to be true
#  if school or val:
#      print("great")
#  elif school:
#      print("good")
#  else:
#      print("bad")

# if len(val3) > val4: 
#     print("greater")
# elif len(val3) == val4:
#     print("equal")
# else:
#     print("lesser")

# print(len(val))

# if len(val3) >= val4 and len(val3) <= val5:
#     print("within range")
# else:
#     print("out of range")

# for i in range(1, 11):
#     if i%2 == 0:
#         print("even")
#     else:
#         print("odd")


# for i in range(1, 11):
#     if i == 7:
#         print("seven")
#         continue
#     print(i)

# for i in range(1, 11):
#     if i%2 == 0:
#         print("even")
#         continue
#     print(i)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

"""function"""

# def first_func():
#     pass

# print(first_func())
# def first_func():
#     print("let explore python function")


# first_func()

# def first_func():
#     return "let explore python function with return"

# print(first_func())

# def first_func(a, b):
#     return "{},{}  are number amd alphabet respectively".format(a, b)

# print(first_func(19, "R"))

# def first_func(name, state="ibadan"):
#     return "{} is presenty in {}".format(name)

# print(first_func("abdulmueez"))

# def first_func(*course, **department):
#     print(course)
#     print(department)

# first_func("comp engr", "mech engr", first=50, second = 30, third= 25)

# def first_func(*arg, **kwage):
#     print(arg)
#     print(kwage)
# course = ["comp engr", "mech engr"]
# department = {"first":50, "second":30, "third":25}

# first_func(*course, **department)


"""getting the number of days in month"""

# month_days = [0, 31, 28, 31, 30, 31 , 30, 31, 31, 30, 31, 30, 31]

# def leap_year(year):
#    return  year % 4 == 0 and (year % 100 != 0 or year % 400  == 0) 


# def days_in_month(year, month):
#     if not  1 <= month <= 12:
#         return "invalid month"
#     elif month == 2 and leap_year(year):
#         return 29
#     else:
#         return month_days[month]




# print(days_in_month(2017, 2))

x = input("what is the value: " )
print(x)