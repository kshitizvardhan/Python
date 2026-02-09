a = 20
b = 40
c = 50

print("The value of a is " + str(a))
print("The value of b is " + str(b))
print("The value of c is " + str(c))

Add = str(a) + str(b) + str(c)
print(Add, type(Add))
intAdd = int(Add)
print(intAdd, type(intAdd))

name = "Kshitiz"
# d = int(name)  # This will raise a ValueError because "Kshitiz" cannot be converted to an integer


x = int("10")    # String "10" becomes Integer 10
y = int(5.99)    # Float 5.99 becomes Integer 5 (drops the decimal)

print(x + 5, y)     # Output: 15

price = float("9.99")  # String "9.99" becomes Float 9.99
whole = float(5)       # Integer 5 becomes Float 5.0

print(price, whole)

# int(), float(), str() are functions used for type casting in Python.



