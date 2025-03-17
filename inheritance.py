# Inheritance allows a new class (child) to take properties from an existing class (parent).

class Animal:  # Parent class
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Child classes
class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Rat(Animal):
    def speak(self):
        print("SQWEEK")


dog = Dog("Scooby")
cat = Cat("Tom")
rat = Rat("Jerry")


print(dog.name)
print('alive:', dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print('alive:', cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(rat.name)
print('alive:', rat.is_alive)
rat.eat()
rat.sleep()
rat.speak()