# FirstAndLast

# def first_and_last(value):
#     first_char = value[0]
#     last_char = value[-1]

#     if value == "":
#         return {
#             "first": "",
#             "last": ""
#         }
#     else:
#         return {
#             "first": first_char,
#             "last": last_char
#         }



# strValue = "kilam"

# print(strValue[::-1])



class KitchenCalculator:
    def calculate_inventory(self):
        customers = 3
        cereal_per_customer = 2.5
        milk_per_customer = 1.25
        
        starting_cereal = 10.0
        starting_milk = 15.0
        
        # 1. Use multiplication to calculate the totals needed
        total_cereal = 2.5 * customers
        total_milk = 1.25 * customers
        
        # 2. Use subtraction to calculate the remaining inventory
        remaining_cereal = starting_cereal - total_cereal
        remaining_milk = starting_milk - total_milk
        
        return remaining_cereal, remaining_milk


def test_calculator():
    # Do not modify this testing wrapper
    calc = KitchenCalculator()
    return list(calc.calculate_inventory())

def solution():
    return test_calculator()


# receip formatter
def receipt_formatter(name, quantity, price):
    subtotal = round((quantity * price), 2)
    tax =  round((subtotal * (7.5/100)), 2)
    total = round((subtotal + tax), 2)

    return f"Customer: {name}\nSubtotal: {subtotal:.1f}\nTax: {tax}\nTotal: {total}"





