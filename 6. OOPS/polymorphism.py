# In programming, it allows you to treat different objects (like a Dog and a Cat) as if they were the same thing 
# (an Animal), even though they behave differently.

# You press the same method, but you get a different behavior depending on the object.
# Already seen Method Overriding in Inheritance, which is a form of Polymorphism.

# Python doesn't care about the type of the object. It only cares about the capabilities (methods/attributes).
# In many languages (like Java), objects strictly need to inherit from the same Parent Class to be polymorphic.
# Python is different. It uses "Duck Typing."
# Duck Typing: "If it looks like a duck and quacks like a duck, it's a duck."
# This means that as long as an object has the methods/attributes you need, you can use it, regardless of its class.

def makeAnimalSpeak(animal):
    print(animal.speak())  # We call the speak method, but we don't care what type of animal it is.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"
    
class Car:
    def speak(self):
        return "Vroom!"
    
animals = [Dog(), Cat(), Duck(), Car()]  # We can put different types of objects in the same list because they all have a speak method.
for animal in animals:
    makeAnimalSpeak(animal)  # Each animal speaks differently, but we use the same function to make them speak.

# Let's add a Car class. A car isn't an animal, but if we give it a speak() method, Python treats it just like the others!
# The function makeAnimalSpeak didn't crash. It just asked the object to speak(), and the object complied.
# This is Duck Typing in action. The type of the object doesn't matter, as long as it has the method we want to call.
# This is a powerful feature of Python that allows for great flexibility and code reuse.
# Polymorphism is a fundamental concept in OOP that allows us to write more flexible and reusable code.