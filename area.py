<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 0d57839 (first-aug)
# # def area_of_triangle(length, breath):
# #     print("__name__", __name__)
# #     return 1/2 * (breath * length)


# # if __name__ == "__main__":
# #     print("i an in area_of_tringle")
# #     a = area_of_triangle(20, 50)
# #     print("area", a)


# def count_down(cups):
#     if cups <= 0:
#         print("Done!")
#         return
#     print("Cup: " + str(cups))
#     count_down(cups - 1)

# count_down(3)


# Implement initials_badge(full_name). Remove leading and trailing spaces, split the name into words, take the first character of each word, convert each initial to uppercase, and return the initials joined with dots. The returned badge should end with a dot.

# def initials_badge(full_name):
#     initials_str = ""
#     full_name_toString = full_name.split(" ")
#     for name in full_name_toString:
#         if name:
#             initials_str += name[0]
#             initials_str += "."
#     return initials_str.upper()

# # Implement error_hint(error_type). Return a helpful debugging hint for common Python errors. For NameError return Check variable names and spelling. For TypeError return Check the types before using an operator. For ValueError return Check whether the value can be converted. For ZeroDivisionError return Check that the denominator is not zero. For IndexError return Check the index is inside the valid range. For anything else return Read the traceback carefully.
# def error_hint(error_type):
#     if error_type == "NameError":
#         return "Check variable names and spelling."
#     elif error_type == "TypeError":
#         return "Check the types before using operator."
#     elif error_type == "ValueError":
#         return "Check whether the value can be converted."
#     elif error_type == "ZeroDivisionError":
#         return "Check that the denominator is not zero."
#     elif error_type == "IndexError":
#         return "Check the index is inside the valid range."
#     else:
#         return "Read the traceback carefully."


# def error_hint(error_type):
#     # Map each error type string to its specific debugging hint
#     hints = {
#         "NameError": "Check variable names and spelling.",
#         "TypeError": "Check the types before using an operator.",
#         "ValueError": "Check whether the value can be converted.",
#         "ZeroDivisionError": "Check that the denominator is not zero.",
#         "IndexError": "Check the index is inside the valid range."
#     }
    
#     # Return the matching hint, or use the default fallback if the error is unknown
#     return hints.get(error_type, "Read the traceback carefully.")

# Implement score_summary(name, a, b, c). Convert the three score values to numbers. If conversion fails, return Invalid score. If any score is below 0 or above 100, return Invalid score. Otherwise calculate the average, round it to 2 decimal places, choose a grade, and return a three-line report with labels Student, Average, and Grade. Grade is A for 90 and above, B for 80 and above, C for 70 and above, and F below 70.
def score_summary(name, a, b, c):
    try:
        conv_a = float(a)
        conv_b = float(b)
        conv_c = float(c)
    except (ValueError, TypeError):
        return "Invalid score"
    
    if score < 0 or score > 100:
        return "Ivalid score"
    avg = round((conv_a + conv_b + conv_c), 2)

    if avg >= 90:
        Grade = "A"
    elif age >= 80 and age < 90:
        Grade = "B"
    elif age >= 70 and age < 80:
        Grade = "C"
    else:
        Grade = "F"
    return Grade
    return f"Student: {name}\nAverage: {avg}\nGrade: {Grade}"
<<<<<<< HEAD
print(score_summary("mueez", 90, 86, 90))
=======
print(score_summary("mueez", 90, 86, 90))
=======
# def area_of_triangle(length, breath):
#     print("__name__", __name__)
#     return 1/2 * (breath * length)


# if __name__ == "__main__":
#     print("i an in area_of_tringle")
#     a = area_of_triangle(20, 50)
#     print("area")

# drinks = ["latte", "espresso", "mocha"]
# loud_drinks = list(map(lambda d: d.upper(), drinks))
# print(loud_drinks)

menu_items = [
    {"name": "Mocha", "price": 5.00},
    {"name": "Espresso", "price": 3.50}
]
# We tell Python: "Look inside the dictionary and pull out the 'price' value to sort"
sorted_menu = sorted(menu_items, key=lambda item: item["price"])
print(sorted_menu)


def add(*args):
    print(sum(args))

add(2,5)


# sorted_val = sorted(menu_items, key=lambda item: item["price"])
# list(map(lambda item, price: price * item, menu_items))

num = [1,6,8]

print(num[::2])

# lis comprehension

# ccomp = [x * 2 for x in num]
# print(ccomp)


full_name = "Mueez,Raheem,malik"
print(full_name[6:12]
)
print(full_name.split(',',1))
>>>>>>> 33d816b (next-push)
>>>>>>> 0d57839 (first-aug)
