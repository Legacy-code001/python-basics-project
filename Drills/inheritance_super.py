# class greeting:
#     def eng(self):
#         print("Hello")

# class noon(greeting):
#     pass
# G = noon()
# G.eng()



# # overidiing child parameter
# class CardboardCup:
#     def get_material(self):
#         return "paper"

# class InsulatedCup(CardboardCup):
#     # Override the parent method completely
#     def get_material(self):
#         return "double-walled paper"

# standard = CardboardCup()
# premium = InsulatedCup()

# print(standard.get_material()) # Output: paper
# print(premium.get_material())  # Output: double-walled paper


# class CardboardCup2:
#     def __init__(self):
#         self.content_capacity = 0
#     def fill(self, litre):
#         self.content_capacity += litre

# class MyCup(CardboardCup2):
#     def __init__(self):
#         super().__init__()
#         self.current_state = True
#     def fill(self, litre):
#         super().fill(litre)
#         # print(f"the state is currently {self.current_state}")

# first_cup = MyCup()
# first_cup.fill(20)

# class CardboardCup:
#     def __init__(self):
#         self.contents_ounces = 0.0
        
#     def fill(self, ounces):
#         self.contents_ounces += ounces

# class InsulatedCup(CardboardCup):
#     def __init__(self):
#         # Run the parent's constructor first!
#         super().__init__()
#         self.has_temp_check = True
        
#     def fill(self, ounces):
#         # 1. Use super() to run the base pouring math
#         super().fill(ounces)
#         # 2. Perform specialized child actions
#         print("Insulation layer activated. Heat is trapped.")

# premium_cup = InsulatedCup()
# premium_cup.fill(8.0)

class Cup:
    def fill(self):
        print("Pouring...")

class SuperCup(Cup):
    def fill(self):
        super().fill()
        print("Locking lid!")

sc = SuperCup()
sc.fill()


# c3 lineariztion
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        print("Left init")
        super().__init__()  # Passes control to the next MRO step, not necessarily Base!

class Right(Base):
    def __init__(self):
        print("Right init")
        super().__init__()

class Child(Left, Right):
    def __init__(self):
        print("Child init")
        super().__init__()

# Instantiate the child
obj = Child()
