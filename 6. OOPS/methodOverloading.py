class Add:
    
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c
    

# In Python, method overloading (having multiple methods with the same name but different parameters) is not supported like in some other languages (e.g., Java or C++).
# If you define multiple methods with the same name, the last one will overwrite the previous ones. So in the above code, the second add method will overwrite the first one, and you will only be able to use the version that takes three parameters.