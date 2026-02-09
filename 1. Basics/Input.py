# The input() function always receives data as a String (text). 
# If you want to use that input for math, you must convert (or "cast") it to a number.

name = input("Enter your name: ")
print("Hello, " + name + "!")

age = input("Enter your age: ")
age = int(age)  # Convert the input string to an integer
print("You will be", age + 1, "next year.")

# Shortcut: You can combine input() and int()/float() in one line:
marks = int(input("Enter your marks: "))
percentage = float(input("Enter your percentage: "))
print("Your marks are", marks)
print("Your percentage is", percentage)

x,y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)

# In order to not write int() or float() multiple times, you can use map():
a, b = map(int, input("Enter two integers separated by space: ").split())
print("Sum:", a + b)