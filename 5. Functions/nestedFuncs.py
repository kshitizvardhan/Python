# Nested Functions is a function defined inside another function.
# The inner function can access the variables of the outer function.

def outerFunction(outerVar):
    print("Outer variable:", outerVar)

    def innerFunction(innerVar):
        print("Inner variable:", innerVar)
        print("Accessing outer variable from inner function:", outerVar)

    innerFunction("Hello from inner function!")


outerFunction("Hello from outer function!")

# Nested functions are often used to create closures, 
# which allow the inner function to remember the state of the 
# outer function even after the outer function has finished executing.

def outerFunction():
    x = 1
    
    def innerFunction():
        # x += 1  # This will cause an error because x is not defined in the inner function's scope
        nonlocal x  # This tells Python to use the x from the outer function's scope
        x += 1
        y = 2
        result = x + y
        return result
    
    return innerFunction()

closureFunction = outerFunction()
print("Result of closure function:", closureFunction)