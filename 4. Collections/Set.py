# A Set is the fourth major collection type in Python. 

# It is distinct because it is unordered and unindexed, 
# but its superpower is that it does not allow duplicates.

# Think of a Set like a bag of unique marbles. 
# You can reach in and grab one, 
# but you can't say "give me the 3rd marble" because they are jumbled up, 
# and you can never have two identical marbles in the bag.

# Sets use curly braces {}, just like dictionaries, but they do not have key-value pairs (no colons).

# Creating a Set
fruits = {"apple", "banana", "cherry", "apple"}  # Note the duplicate "apple"
print(fruits)  # Output: {'banana', 'cherry', 'apple'} - duplicates are removed 

# Checking the type of the set
print(type(fruits))  # Output: <class 'set'>

# Length of the set (number of unique elements)
print(len(fruits))  # Output: 3

# Adding an element to a Set
fruits.add("orange")

# Removing an element from a Set
fruits.remove("banana")  # Raises KeyError if "banana" is not found
fruits.discard("banana")  # Does not raise an error if "banana" is not found
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Checking if an element exists in a Set
if "cherry" in fruits:
    print("Cherry is in the set!")

# Iterating through a Set
for fruit in fruits:
    print(fruit)

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: Combines all unique elements from both sets
union_set = A.union(B)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements common to both sets
intersection_set = A.intersection(B)
print("Intersection:", intersection_set)  # Output: {3, 4}

# Difference: Elements in A but not in B
difference_set = A.difference(B)
print("Difference (A - B):", difference_set)  # Output: {1, 2}

# Symmetric Difference: Elements in either A or B but not in both
symmetric_difference_set = A.symmetric_difference(B)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 5, 6}

# Frozen Set: An immutable version of a set
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print("Frozen Set:", frozen_fruits)  # Output: frozenset({'apple', 'banana', 'cherry'})
print("Type of Frozen Set:", type(frozen_fruits))  # Output: <class 'frozenset'>
# You cannot add or remove elements from a frozen set
# frozen_fruits.add("orange")  # This will raise an AttributeError
# Note: Sets are particularly useful when you need to ensure that a collection of items is unique,
# such as when tracking unique user IDs, tags, or categories.

# Adding multiple elements to a Set
fruits.update(["kiwi", "mango", "apple"])  # "apple" is already in the set, so it won't be added again
print(fruits) 

# Clearing all elements from a Set
fruits.clear()
print(fruits)  # Output: set() - an empty set

# Merging a Set with another Set
A.update(B)
print("Updated Set A:", A)  # Output: {1, 2, 3, 4, 5, 6}

# Removing and returning an arbitrary element from a Set
removed_element = A.pop()
print("Removed Element:", removed_element)
print("Set A after pop:", A)
# Note: Since sets are unordered, you cannot predict which element will be removed by pop()

# Keeping only dupllicates while joining two sets
# 1. Create the set first
my_set = {"a", "b", "c", "d"}

# 2. Update it (don't assign this line to a variable!)
my_set.intersection_update({"c", "d", "e", "f"})

# 3. Print the original variable
print("Modified Set:", my_set)
# Output: {'c', 'd'}

# Keeping all values except duplicates while joining two sets
# 1. Create the set first
my_set2 = {"a", "b", "c", "d"}

# 2. Update it (don't assign this line to a variable!)
my_set2.symmetric_difference_update({"c", "d", "e", "f"})

# 3. Print the original variable
print("Modified Set:", my_set2)
# Output: {'a', 'b', 'e', 'f'}

# Another way is direct this, but dont put update in the function name at last
# Use .intersection() instead of .intersection_update()
C = {"a","b","c","d"}.intersection({"c","d","e","f"})
print("Set C:", C)
# Output: {'c', 'd'}

# Use .symmetric_difference() instead of .symmetric_difference_update()
D = {"a","b","c","d"}.symmetric_difference({"c","d","e","f"})
print("Set D:", D)
# Output: {'a', 'b', 'e', 'f'}