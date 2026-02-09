# Dictionary is like a real-world dictionary or a phone book. It stores data in Key-Value Pairs.

# Key: The unique label (like a word in a dictionary or a contact name).
# Value: The data associated with that label (like the definition or the phone number).

# Creating a Dictionary
student = {
    "name": "Kshitiz",        # Key: "name", Value: "Kshitiz"
    "age": 21,                # Key: "age", Value: 21
    "is_student": True,        # Key: "is_student", Value: True
    "city": "New York"      # Key: "city", Value: "New York"
}

# Accessing Values
# Unlike lists, you do not use numbers (indexes) to find things. You use the Key
print(student["name"])      # Output: Kshitiz
print(student["age"])       # Output: 21

# To avoid crashing your program, you can use the .get() method. 
# It returns None if the key isn't found.
print(student.get("city"))  # Output: New York

# Dictionaries are mutable (changeable), so you can modify them after creation.
student["age"] = 22         # Update age to 22

# Add a NEW key-value pair
student["job"] = "Engineer"

# Print the entire dictionary
print(student)

# Checking the type of the dictionary
print(type(student))        # Output: <class 'dict'>

# Checking the type of a value in the dictionary
print(type(student["name"])) # Output: <class 'str'>
print(type(student["age"]))  # Output: <class 'int'>

# Length of the dictionary (number of key-value pairs)
print(len(student))         # Output: 5

# Checking if a key exists in the dictionary
if "name" in student:
    print("Name is in the dictionary!")

# Checking if a key does not exist in the dictionary
if "address" not in student:
    print("Address is not in the dictionary!")

# Removing a key-value pair
del student["is_student"]  # Removes the key "is_student" and its value
print(student)

# Accessing a non-existent key will raise a KeyError
# print(student["is_student"])  # This will raise a KeyError because "is_student" has been deleted

# To avoid KeyError, you can use the .get() method which returns None if the key is not found
print(student.get("is_student"))  # Output: None

# You can also use the .pop() method to remove a key and get its value at the same time
job = student.pop("job")  # Removes "job" and returns its value
print("Popped job:", job)  # Output: Popped job: Engineer
print(student)  # Output: {'name': 'Kshitiz', 'age': 22, 'city': 'New York'}

# Accessing all keys, values, or key-value pairs
print(student.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(student.values())  # Output: dict_values(['Kshitiz', 22, 'New York'])
print(student.items())   # Output: dict_items([('name', 'Kshitiz'), ('age', 22), ('city', 'New York')])

# Looping through a dictionary
for key in student:
    print(key, ":", student[key])  # Output: name : Kshitiz, age : 22, city : New York

# You can also loop through keys and values using .items()
for key, value in student.items():
    print(key, ":", value)  # Output: name : Kshitiz, age : 22, city : New York


# Referencing vs Copying
student_ref = student  # This does NOT create a new dictionary, it just creates a reference
student_ref["age"] = 23  # This will change the age in both student and student_ref
print(student)       # Output: {'name': 'Kshitiz', 'age': 23, 'city': 'New York'}
print(student_ref)   # Output: {'name': 'Kshitiz', 'age': 23, 'city': 'New York'}

# To create an actual copy that does not affect the original, use the .copy() method
student_copy = student.copy()
student_copy["age"] = 24  # This will only change the age in student_copy
print(student)       # Output: {'name': 'Kshitiz', 'age': 23, 'city': 'New York'}
print(student_copy)  # Output: {'name': 'Kshitiz', 'age': 24, 'city': 'New York'}



# Clearing a Dictionary
student.clear()  # This removes all key-value pairs from the dictionary
print(student)  # Output: {}

# Deleting a Dictionary
del student  # This deletes the entire dictionary
# print(student)  # This will raise a NameError because student has been deleted

# Nested Dictionaries
# A dictionary can contain another dictionary as a value.
students = {
    "student1": {
        "name": "Sakshi",
        "age": 20
    },
    "student2": {
        "name": "Kshitiz",
        "age": 22
    }
}

print(students["student1"]["name"])  # Output: Sakshi
print(students["student2"]["age"])   # Output: 22