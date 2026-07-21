# Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

# Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

# Store your first, middle and last name in three different variables and then print your full name using these variables

# Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue



# breaks = 5
# # print(breaks)

# birth_year = 1999
# current_year = 2026

# your_age = current_year - birth_year
# # print(your_age)

# first_name = "Abdulraheem"
# middle_name = "Abdulmueez"
# last_name = "Opeyemi"

# print("My full name is: "first_name, middle_name, last_name)


# You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
# You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
# Print binary representation of number 17

# length_of_field = 92
# breath_of_field = round(48.8)

# area = str(length_of_field * breath_of_field) + "m^2"
# print(area)

# quantity_of_Chips = 9
# cost_of_one = 1.49
# cost_Of_9 = 9 * 1.49
# amount_paid = 20
# amount_received = str(amount_paid - cost_Of_9) + "dollar"
# print(amount_received)

# length_of_birthroom = 5.5 
# area = 5.5 ** 2
# size_of_tiles = 500
# number_of_needed_tiles = area * size_of_tiles
# print(number_of_needed_tiles)

# print(bin(17)[2:])

# Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.


# street = "okesanya\n"
# city = "Ibadan\n"
# country = "Nigeria\n"

# # address = """{}, 
# # {},
# #  {}""".format(street, city, country)


# address = street + city + country
# print(address)

statement = "Earth revolves around sun"
# print(statement[:5])
# print(statement[-3:])

fruit = 5
vegetables = 3

# print("i eat", fruit, "fruits" , vegetables, "veggies")
s='maine 200 banana khaye'

s = "maine 10 samosa khaye"
print(s)
