# 1. The Core Concept: Class vs. Object
# Think of a car factory.

# Class (The Blueprint): The engineering drawing of a Ferrari. 
# It defines that every Ferrari has 4 wheels, an engine, and a color. 
# You cannot drive the drawing.

# Object (The Instance): The actual red Ferrari sitting in your driveway. 
# You can drive this. 
# You can build 1,000 unique cars from that one single blueprint.

# 2. Defining a Class
class A:
    pass  # This is a placeholder that does nothing. We will add attributes and methods later.

# 3. The __init__ Method (The Constructor)
# This is a special function that runs automatically whenever you create a new object. 
# It sets up the initial state (the "ingredients").
# It must be named __init__ (with two underscores on each side).

# 4. What is self?
# You will see self everywhere in Python classes.
# self refers to "this specific object right here."
# When you create a red car, self.color is Red.
# When you create a blue car, self.color is Blue.
# Python passes self automatically; you don't type it when calling functions,
#  but you must include it when defining them.

# Now let's put it all together and create a Car class with an __init__ method and some attributes.

class Car:
    # 1. The Blueprint (Class Constructor)
    def __init__(self, make, model, year, color):
        self.make = make  # The make of the car (e.g., "Ferrari")
        self.model = model  # The model of the car (e.g., "488 Spider")
        self.year = year  # The year the car was made (e.g., 2020)
        self.color = color  # The color of the car (e.g., "Red")
        self.speed = 0  # The current speed of the car, initialized to 0, Default value

    # 2. Methods (Functions inside a Class/Actions the Car can perform)

    def drive(self):
        self.speed = 60  # Set the car's speed to 60
        print(f"The {self.color} {self.make} {self.model} is now driving at {self.speed} mph.")

    def stop(self):
        self.speed = 0  # Set the car's speed to 0
        print(f"The {self.color} {self.make} {self.model} has stopped.")

    def honk(self):
        print(f"The {self.color} {self.make} {self.model} goes 'Beep Beep!'")
    
    def accelerate(self, increase):
        self.speed += increase  # Increase the car's speed by the specified amount
        print(f"The {self.color} {self.make} {self.model} accelerates to {self.speed} mph.")

# 5. Creating Objects (Instances of the Class)
myCar = Car("Ferrari", "488 Spider", 2020, "Red")
print(myCar.make)  # Output: Ferrari
print(myCar.model)  # Output: 488 Spider
print(myCar.year)  # Output: 2020
print(myCar.color)  # Output: Red

myCar.drive()  # Output: The Red Ferrari 488 Spider is now driving at 60 mph.
myCar.accelerate(20)  # Output: The Red Ferrari 488 Spider accelerates to 80 mph.
myCar.stop()  # Output: The Red Ferrari 488 Spider has stopped.
myCar.honk()  # Output: The Red Ferrari 488 Spider goes 'Beep Beep!'


class student:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age 

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
student1 = student("Kshitiz", 18)
print(student1.getName())  # Output: Kshitiz
print(student1.getAge())  # Output: 18
student1.setName("Kshitiz Vardhan")
student1.setAge(19)
print(student1.getName())  # Output: Kshitiz Vardhan
print(student1.getAge())  # Output: 19