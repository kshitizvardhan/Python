# Use a for loop when you know how many times you want to repeat something, 
# or when you want to look at every item in a collection (like a list of names or a string of text).

# A. Using range()
# The range() function generates a sequence of numbers.
# range(5): Generates 0, 1, 2, 3, 4 (starts at 0, stops before 5).
# range(1, 6): Generates 1, 2, 3, 4, 5.

# (Inclusive Start and Exclusive End)
for i in range(0,5):
    print("Iteration:", i)

# (Inclusive Start, Exclusive End, Step)
for i in range(1, 11, 2):  # Prints odd numbers from 1 to 10
    print("Odd Number:", i)

# (End Only)
for i in range(5):  # Equivalent to range(0, 5)
    print("iteration:", i)

# B. Looping through a collection (like a string or list)
# Looping through a string
word = "Python"
for letter in word:
    print("Letter:", letter)

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# C. Nested Loops
# A loop inside another loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print("i:", i, "j:", j)

# D. Using else with for loop
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop completed!")

# E. Using break and continue
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print("Odd Number:", i)

# F. Using enumerate() to get index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

# G. Using zip() to loop through multiple collections
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, "is", age, "years old.")

