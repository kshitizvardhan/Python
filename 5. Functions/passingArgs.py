# Can pass multiple arguments to a function, just separate them with commas.
def add(a,b):
    return a + b

print(add(5, 3))




# Parameters can have default values. If we call the function without an argument, it uses the default value.
def greet(name="Guest"):
    print("Hello " + name + "!")
    print("Welcome to Python programming.")

greet()  # Uses default value "Guest"
greet("Kshitiz")  # Overrides default value with "Kshitiz"

# You can also have functions with multiple parameters, and you can mix default and non-default parameters.
def greet(name, greeting="Hello"):
    print(greeting + " " + name + "!")
    print("Welcome to Python programming.")

greet("Kshitiz")  # Uses default greeting "Hello"
greet("Kshitiz", "Hi")  # Overrides default greeting with "Hi"

# You can also use keyword arguments to specify which parameter you are passing a value for, regardless of their position.
greet(greeting="Hey", name="Kshitiz")  # Uses keyword arguments to specify parameters

# Parameters can be of any data type, and you can even pass multiple parameters of different types to a function.





# Passing by reference vs passing by value:
# In Python, mutable objects (like lists and dictionaries) are passed by reference,
# while immutable objects (like integers and strings) are passed by value.

def modifyList(myList):
    print("Inside function before modification:", myList)
    myList.append(4)
    # myList = [32, 52, 61] # --> This will not modify the original list because it creates a new list
    print("Inside function after modification:", myList)

myNumbers = [1, 2, 3]
modifyList(myNumbers)
print("Outside function:", myNumbers)  # The original list is modified because it's mutable

def modifyString(myString):
    print("Inside function before modification:", myString)
    myString += " World!"  # This creates a new string, as strings are immutable
    print("Inside function after modification:", myString)

myGreeting = "Hello"
modifyString(myGreeting)
print("Outside function:", myGreeting)  # The original string is unchanged because it's immutable



# *args and **kwargs:
# *args allows you to pass a variable number of non-keyword arguments to a function.

def sumAll(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sumAll(1, 2, 3))  # Output: 6
print(sumAll(4, 5))     # Output: 9

# **kwargs allows you to pass a variable number of keyword arguments to a function.
def printInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printInfo(name="Kshitiz", age=18, city="New York")