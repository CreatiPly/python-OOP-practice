# When a child class inherits from a parent class which itself is inheriting from another parent class 

# Grandparent class
class Animal:
    def eat(self):
        print("This animal is eating")

# Parent classes
class Pray(Animal):
    def flee(self):
        print("This animal is fleeing from the predator")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting the pray")


# Child classes
class Rabbit(Pray):   # Inherits from the Pray class
    pass

class Hawk(Predator):   # Inherits from the Predator class
    pass

class Fish(Pray, Predator):   # Inherits from both the Pray and the Predator class (MULTIPLE INHERITANCE)
    pass


rabbit = Rabbit()

rabbit.flee()
# rabbit.hunt()   rabbit object does not have the method hunt BC it is inheriting only from Pray class 
rabbit.eat()   # Method from the grandparent class

hawk = Hawk()

hawk.hunt()
# hawk.flee()   hawk object does not have the method flee BC it is inheriting only from Predator class
hawk.eat()   # Method from the grandparent class


fish = Fish()

# the object fish have both hunt and flee methods BC it is inheriting from both Pray and Predator classes
fish.hunt()
fish.flee()
fish.eat()   # Method from the grandparent class