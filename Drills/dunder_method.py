# class CardboardCup:
#     def __init__(self, size, drink):
#         self.size = size
#         self.drink = drink

# alice_cup = CardboardCup("large", "Latte")
# print(alice_cup.drink)
# print(alice_cup)


# class CardboardCup2:
#     def __init__(self, size, drink):
#         self.size = size
#         self.drink = drink
        
#     # The __str__ method MUST return a string
#     def __str__(self):
#         return f"{self.size.capitalize()} {self.drink} Cup"

# alice_cup = CardboardCup2("large", "Latte")
# print(alice_cup) # Output: Large Latte Cup


# # If a list contains multiple objects, printing the list will execute the __repr__ method of each object, not __str__.

# class CardboardCup:
#     def __init__(self, size, drink):
#         self.size = size
#         self.drink = drink
        
#     def __repr__(self):
#         # Format the output to look like the instantiation call
#         return f"CardboardCup('{self.size}', '{self.drink}')"

# cup_list = [CardboardCup("small", "Espresso"), CardboardCup("large", "Latte")]
# print(cup_list) # Output: [CardboardCup('small', 'Espresso'), CardboardCup('large', 'Latte')]

# # len(my_cup) is called. Python automatically maps this to my_cup.__len__().
# class CardboardCup:
#     def __init__(self, ounces):
#         self.contents_ounces = float(ounces)
        
#     # __len__ must return a standard integer
#     def __len__(self):
#         return int(self.contents_ounces)

# my_cup = CardboardCup(8.5)
# current_volume = len(my_cup)

# class CardboardCup3:
#     def __init__(self, size, drink):
#         self.size = size
#         self.drink = drink
    
#     def __eq__(self, other):
#         if not isinstance(other, CardboardCup3):
#             return False

#         return self.size == other.size and self.drink == other.drink

# cup3a = CardboardCup3("big", "coke")
# cup3b = CardboardCup3("big", "coke")
# print(cup3a == cup3b)



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x * other.x, self.y * other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(5, 9)
v2 = Vector(9, 4)
v3= [Vector(5,8), Vector(67, 7), (90)]

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1)
print(v3)