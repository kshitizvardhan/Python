# A list is an ordered collection of items.
# In Python, lists are created using square brackets [], and items are separated by commas.
# Lists are: 
# Ordered: The items stay in the order you put them.
# Mutable: You can add, remove, or change items after the list is created.
# Mixed Types: A list can hold anything (numbers, strings, even other lists!).

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [5, 6, 7]]

# Accessing List Items
# To get a specific item out of a list, you use its Index (position).
# You can also count backwards using negative numbers. -1 is always the last item.
# The first item is at index 0.
# The second item is at index 1

print(fruits[0])      # Output: apple
print(fruits[1])      # Output: banana
print(fruits[-1])     # Output: cherry

# Printing the List
print(fruits)

# Checking Type
print(type(fruits))   # Output: <class 'list'>

# Checking Length
print(len(fruits))

# Checking type of an item in the list
print(type(fruits[0])) # Output: <class 'str'>

# Checking if an item exists in the list
if "banana" in fruits:
    print("Banana is in the list!")

# Checking if an item does not exist in the list
if "orange" not in fruits:
    print("Orange is not in the list!")

# Modifying List Items
fruits[1] = "blueberry"  # Change "banana" to "blueberry"
print(fruits) # Since lists are mutable, this works!

# Adding Items to a List
fruits.append("orange")  # Adds "orange" to the end of the list
print(fruits)

# Inserting Items at a Specific Position
fruits.insert(1, "kiwi")  # Inserts "kiwi" at index 1
print(fruits)

# Removing Items from a List
fruits.remove("cherry")  # Removes "cherry" from the list
print(fruits)

popped_fruit = fruits.pop()  # Removes and returns the last item
print("Popped fruit:", popped_fruit)

fruits.pop(1)  # Removes the item at index 1

# Accessing Sublists (Slicing)
print(fruits[1:3])  # Items from index 1 to 2 (3 is excluded)
print(fruits[:2])   # Items from start to index 1
print(fruits[2:])   # Items from index 2 to the end

# Extending a List
more_fruits = ["mango", "papaya"]
fruits.extend(more_fruits)  # Adds items from more_fruits to fruits
print(fruits)

# Sorting a List
fruits.sort()  # Sorts the list in alphabetical order
print(fruits)

# Reversing a List
fruits.reverse()  # Reverses the order of the list
print(fruits)

# Clearing a List
fruits.clear()  # Removes all items from the list
print(fruits)  # Output: []

# Note: After clearing, the list still exists but is empty.
# To delete the list entirely, you can use the del statement:
del fruits
# print(fruits)  # This would raise an error since fruits is deleted.

li = [13, 22, 39, 41, 59]

# Looping through a list
for item in li:
    print("Item:", item)

# Using enumerate() to get index and value
for index, item in enumerate(li):
    print("Index:", index, "Item:", item)

# Using list comprehension to create a new list
new_list = [x * 2 for x in li]
print("New List:", new_list)

new_list_filtered = [x for x in li if x > 30]
print("Filtered List (items > 30):", new_list_filtered)

# Copying a List
copied_list = li.copy()
print("Copied List:", copied_list)

# Note: Lists can contain duplicate items.
duplicate_list = [1, 2, 2, 3, 4, 4, 4]
print("List with duplicates:", duplicate_list)

# Concatenating Lists
combined_list = li + [100, 200, 300]
print("Combined List:", combined_list)

# Nesting Lists
nested_list = [li, [100, 200, 300], ["a", "b", "c"]]
print("Nested List:", nested_list)
print(nested_list[1][2]) # Accessing "300" from the nested list

# Converting other collections to a list
string_to_list = list("hello")
print("String to List:", string_to_list)

set_to_list = list({1, 2, 3, 4})
print("Set to List:", set_to_list)

# Note: The order of items in the list converted from a set may vary since sets are unordered.

# List Methods Summary:
# append(), insert(), remove(), pop(), clear(), extend(), sort(), reverse(), copy()
# Slicing: list[start:end], list[:end], list[start:]
# Membership: item in list, item not in list
# Length: len(list)
# Indexing: list[index], list[-index]
# Looping: for item in list, for index, item in enumerate(list)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name + " is " + str(age) + " years old.")

