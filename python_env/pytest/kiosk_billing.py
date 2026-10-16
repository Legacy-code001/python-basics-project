# kiosk_billing.py

def calculate_subtotal(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Inputs cannot be negative!")
    return price * quantity

def apply_discount(total, discount_rate):
    return total * (1.0 - discount_rate)



'''multiple testin'''
# kiosk.py

class CoffeeKiosk:
    def __init__(self, beans_grams, water_ml):
        self.beans = beans_grams
        self.water = water_ml

    def brew_espresso(self):
        if self.beans < 18.0 or self.water < 30.0:
            raise ValueError("Insufficient ingredients!")
        self.beans -= 18.0
        self.water -= 30.0



# testted objet will import this, check the test