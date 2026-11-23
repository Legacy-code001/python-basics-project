# class BlockMould:
#     def __init__(self, size, typ):
#         self.size = size
#         self.color = "empty"
#         self.typ = typ
    
# block9 = BlockMould("nine", "six")
# block9.size = "ten"
# block9.color = "green"
# print(block9.color)


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def __str__(self):
#         return f"car {self.brand} {self.model}"

#     def __repr__(self):
#         return f"car(brand='{self.brand}' model='{self.model}')"


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def __str__(self):
#         # Friendly output for everyday users
#         return f"{self.brand} {self.model}"

#     def __repr__(self):
#         # Precise output for debugging
#         return f"Car(brand='{self.brand}', model='{self.model}')"

# # ---- Testing the Outputs ----
# my_car = Car("Toyota", "Camry")

# # 1. Triggers __str__
# print(my_car)        # Output: Toyota Camry
# print(str(my_car))   # Output: Toyota Camry

# # 2. Triggers __repr__
# print(repr(my_car))  # Output: Car(brand='Toyota', model='Camry')

# # 3. Collections (lists, dicts) display their contents using __repr__
# car_list = [my_car]
# print(car_list)      # Output: [Car(brand='Toyota', model='Camry')]



# my_car = Car("camry", "Toyota")
# print(my_car)
# print(repr(my_car))


class WorkflowDemo:
    def __new__(cls, *args, **kwargs):
        print("1. __new__ is building the object memory space...")
        # Create the actual object instance
        instance = super().__new__(cls)
        return instance

    def __init__(self, data):
        print("2. __init__ is configuring the object attributes...")
        # Populate the instance
        self.data = data

# Trigger the instantiation and initialization workflow
obj = WorkflowDemo("Python Data")
