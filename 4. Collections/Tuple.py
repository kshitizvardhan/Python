# Tuple: Immutable (Once created, it cannot be changed).

# Think of a List as a whiteboard (you can erase and rewrite) 
# and a Tuple as a stone tablet (carved permanently).

# We use parentheses () instead of square brackets []

# Creating a tuple
student = ("Kshitiz", 21, True, "New York") # A tuple with 4 elements(mixed data types)
print(student)

# Accessing elements in a tuple (same as lists)
print(student[0])  # Output: Kshitiz
print(student[1])  # Output: 21
print(student[-1]) # Output: New York (last element)

# Tuples are immutable, so the following line would raise an error if uncommented
# student[1] = 22  # This will raise a TypeError
# However, you can create a new tuple by concatenation
new_student = student + ("Engineer",)  # Adding a new element
print(new_student)  # Output: ('Kshitiz', 21, True, 'New York', 'Engineer')

# Length of the tuple
print(len(student))  # Output: 4

# Checking the type of the tuple
print(type(student))  # Output: <class 'tuple'>

# Tuples can contain duplicate values
duplicates = (1, 2, 2, 3, 4, 4, 4)
print(duplicates)  # Output: (1, 2, 2, 3, 4, 4, 4)

# Tuple unpacking
name, age, is_student, city = student
print(name)        # Output: Kshitiz
print(age)         # Output: 21
print(is_student)  # Output: True
print(city)       # Output: New York

# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])      # Output: (3, 4)
print(nested_tuple[2][0])   # Output: 3
print(nested_tuple[3][1])   # Output: 6

# Iterating through a tuple
for item in student:
    print(item)

# Checking if an element exists in a tuple
if "Kshitiz" in student:
    print("Kshitiz is in the tuple!")   

# Creating a tuple with a single element
single_element_tuple = (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
# Without the comma, it would be considered as an integer
print(type((42)))  # Output: <class 'int'>
print(type(42))    # Output: <class 'int'>

# Slicing a tuple
print(student[1:3])  # Output: (21, True)
print(student[:2])   # Output: ('Kshitiz', 21)
print(student[2:])   # Output: (True, 'New York')

# Tuples are often used for fixed collections of items, like coordinates (x, y)
point = (10, 20)
print("X coordinate:", point[0])  # Output: X coordinate: 10
print("Y coordinate:", point[1])  # Output: Y coordinate: 20

# Tuples can be used as keys in dictionaries because they are immutable
coordinates_dict = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}
print(coordinates_dict[(10, 20)])  # Output: Point A

# Converting a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4)

# Converting a tuple to a list
converted_list = list(student)
print(converted_list)  # Output: ['Kshitiz', 21, True, 'New York']

# Note: Since tuples are immutable, they do not have methods like append(), remove(), or pop() that lists have.

# However, they do have count() and index() methods.
index_of_21 = student.index(21)
print("Index of 21 in student tuple:", index_of_21)  # Output: Index of 21 in student tuple: 1

# Counting occurrences of an element
count_of_4 = duplicates.count(4)
print("Number of times 4 appears:", count_of_4)  # Output: Number of times 4 appears: 3

# Tuples are generally faster than lists for iteration and access due to their immutability.
# This makes them a preferred choice for read-only data.
