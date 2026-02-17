# Functions are the building blocks of organized code.
# They allow us to group a set of statements together to perform a specific task.
# To define a function, we use the def keyword, followed by the function name and parentheses ().
# The code block within every function starts with a colon (:) and is indented.

def greet():
    print("Hello World !")
    print("Welcome to Python programming.")

# To call a function, we simply use its name followed by parentheses.
greet()

# A function becomes much more useful if it can handle different data. 
# We pass data into functions using parameters (often called arguments).
# You put variable names inside the parentheses ().

def greet(name):
    print("Hello " + name + "!")
    print("Welcome to Python programming.")


greet("Kshitiz")
