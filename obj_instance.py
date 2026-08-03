# class CoffeeShop:
#     # Class attribute (shared by all instances)
#     shop_name = "Python Brew"

#     def __init__(self, blend, price):
#         # Instance attributes (unique to each object)
#         self.blend = blend
#         self.price = price

#     # 1. Instance Method
#     def describe_coffee(self):
#         # Accesses individual object data via 'self'
#         return f"{self.blend} costs ${self.price} at {self.shop_name}."

#     # 2. Class Method
#     @classmethod
#     def set_shop_name(cls, new_name):
#         # Modifies class-level data via 'cls'
#         cls.shop_name = new_name

#     # 3. Static Method
#     @staticmethod
#     def is_caffeinated(drink_name):
#         # Independent utility; doesn't use 'self' or 'cls'
#         return "decaf" not in drink_name.lower()


# Implement password_strength(password). Return Weak if the password has fewer than 8 characters. Return Medium if it has at least 8 characters but does not contain both letters and digits. Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. Students may need to research isalpha and isdigit.

# Implement delivery_fee(order_total, distance_km, is_member). If order_total is below 0 or distance_km is below 0, return Invalid input. If is_member is true and order_total is at least 5000, return 0. If distance_km is less than or equal to 5, return 500. If distance_km is less than or equal to 15, return 1000. Otherwise return 2000.

# def delivery_fee(order_total, distance_km, is_member):
#     if order_total < 0 or distance_km < 0:
#         return "Invalid input"
#     if is_member is True and order_total >= 5000:
#         return 0
#     if distance_km  <= 5:
#         return 500
#     if distance_km <= 15:
#         return 1000
#     return 2000


# Implement exact_calculator(left, operator, right). Convert left and right to numbers. Support addition, subtraction, multiplication, division, remainder, and exponent. If either number cannot be converted, return Invalid number. If the operator is not supported, return Invalid operator. If division or remainder uses zero on the right side, return Cannot divide by zero. Round numeric results to 2 decimal places.

def exact_calculator(left, operator, right):
    try:
        conv_left = float(left)
        convert_right = float(right)
    except (ValueError, TypeError):
        return "Invaid number"
    
    if operator == "+":
        return round((conv_left + convert_right), 2)
    if operator == "-":
        return round((conv_left - convert_right), 2)
    if operator == "*":
        return round((conv_left * convert_right), 2)
    if operator == "/" and convert_right == 0:
        return "Cannot divide by zero"
    else:
        return  round((conv_left / convert_right), 2)
    if operator == "%" and convert_right == 0:
        return "Cannot divide by zero"
    else:
        return round((conv_left % convert_right), 2)
    if operator == "**":
        return round((conv_left ** convert_right), 2)
    
    return "Invlid operator"
    
print(exact_calculator("5", "%", "8"))