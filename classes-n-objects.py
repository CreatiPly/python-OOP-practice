# A class is a blueprint for creating objects. Objects are instances of classes.

# Defining a class
class Car:
    def __init__(self, brand, model, year):   # __init__ is the constructor that runs when an object is created
        # self represents the current object instance 
        self.brand = brand   # Attribute 1
        self.model = model   # Attribute 2
        self.year = year     # Attribute 3

    def display_info(self):  # Method (Function inside a class)
        return f"{self.brand} {self.model}, Year: {self.year}"

# Creating objects
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Toyota", "Corolla", 2020)

# Using the method
print(car1.display_info())  # Output: Tesla Model S, Year: 2022
print(car2.display_info())  # Output: Toyota Corolla, Year: 2020
