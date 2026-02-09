# Arithmetic Operators
print("Addition:", 5 + 3)          # Addition
print("Subtraction:", 10 - 2)      # Subtraction
print("Multiplication:", 4 * 2)    # Multiplication
print("Division:", 16 / 4)         # Division
print("Floor Division:", 17 // 3)  # Floor Division -  removes the decimal part
print("Modulus:", 10 % 3)          # Modulus
print("Exponentiation:", 2 ** 3)   # Exponentiation (2^3 = 2*2*2)

# Comparison Operators
x = 10
y = 5
print("x == y:", x == y)   # Equal to
print("x != y:", x != y)   # Not equal to  
print("x > y:", x > y)     # Greater than
print("x < y:", x < y)     # Less than
print("x >= y:", x >= y)   # Greater than or equal to
print("x <= y:", x <= y)   # Less than or equal to

# Logical Operators
a = True
b = False   
print("a and b:", a and b)  # Logical AND
print("a or b:", a or b)    # Logical OR
print("not a:", not a)      # Logical NOT

# Assignment Operators
num = 10
print("Initial num:", num)
num += 5
print("After num += 5:", num)
num *= 2
print("After num *= 2:", num)
num -= 4
print("After num -= 4:", num)
num /= 2
print("After num /= 2:", num)
num %= 3
print("After num %= 3:", num)


# Bitwise Operators
p = 6  # In binary: 110
q = 3  # In binary: 011
print("p & q (AND):", p & q)   # Bitwise AND
print("p | q (OR):", p | q)    # Bitwise OR
print("p ^ q (XOR):", p ^ q)   # Bitwise XOR
print("~p (NOT):", ~p)         # Bitwise NOT
print("p << 1 (Left Shift):", p << 1)  # Left Shift
print("p >> 1 (Right Shift):", p >> 1) # Right Shift

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)        # Checks if 3 is in the list
print("6 not in my_list:", 6 not in my_list) # Checks if 6 is not in the list

# Identity Operators
m = 10
n = 10
print("m is n:", m is n)         # Checks if m and n refer to the same object
print("m is not n:", m is not n) # Checks if m and n do not refer to the same object

# Note: In Python, 'is' checks for identity (same memory location), while '==' checks for equality (same value).
# By default, small integers and strings may refer to the same object in memory due to interning.
# However, for larger objects, 'is' and '==' may yield different results.

# Example to illustrate the difference between 'is' and '=='
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2:", list1 == list2)   # True, because values are the same
print("list1 is list2:", list1 is list2)   # False, because they are different objects in memory