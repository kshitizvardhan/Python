# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def eat(self):
        return "Eating food"

    def sleep(self):
        return "Sleeping"
    
    def move(self):
        return "Moving around"
    
# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class to initialize the name
        self.breed = breed  # Additional attribute specific to Dog

    def speak(self): # Method overriding: The Dog class provides its own implementation of the speak method, which overrides the one in the Animal class.
        return "Bhow Bhow!"
    
    def fetch(self):
        return "Fetching the ball!"
    
myDog = Dog("Buddy", "Golden Retriever")
print(myDog.name)  # Output: Buddy (Inherited from Animal)
print(myDog.breed)  # Output: Golden Retriever (Specific to Dog)
print(myDog.speak())  # Output: Bhow Bhow! (Overridden method)
print(myDog.eat())  # Output: Eating food (Inherited from Animal)
print(myDog.move())  # Output: Moving around (Inherited from Animal)
print(myDog.fetch())  # Output: Fetching the ball! (Specific to Dog)
print(myDog.sleep())  # Output: Sleeping (Inherited from Animal)
print(myDog.__dict__)  # Output: {'name': 'Buddy', 'breed': 'Golden Retriever'} (Shows the attributes of the Dog instance)
print(issubclass(Dog, Animal))  # Output: True (Checks if Dog is a subclass of Animal)
print(isinstance(myDog, Dog))  # Output: True (Checks if myDog is an instance of Dog)
print(isinstance(myDog, Animal))  # Output: True (Checks if myDog is an instance of Animal, which is true because Dog inherits from Animal)
print(isinstance(myDog, object))  # Output: True (Checks if myDog is an instance of object, which is true because all classes in Python inherit from object)
print(super(Dog, myDog).speak())  # Output: Some sound (Calls the speak method of the parent class Animal using super()) 

# The super() function allows you to call a method from the parent class inside the child class. 
# It is most commonly used in __init__ to handle the setup of inherited attributes.

# 4. Types of Inheritance
# Python is flexible and supports different structures:
# Single Inheritance: Child inherits from one Parent (A -> B).
# Multiple Inheritance: Child inherits from two or more Parents (A, B -> C).
# Example: A FlyingCar inherits from both Car and Airplane.
# Multilevel Inheritance: Child inherits from a Parent, who inherited from a Grandparent (A -> B -> C).