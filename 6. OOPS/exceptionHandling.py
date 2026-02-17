# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
a=b=0

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
    print("Result:", result)
except ZeroDivisionError:
    result = None # This is a common way to indicate that the result is undefined due to division by zero.
    print("Error: You cannot divide by zero!")
except ValueError:
    result = None # This is a common way to indicate that the result is undefined due to invalid input.
    print("Error: Please enter valid integers!")
except Exception as e:
    result = None # This is a common way to indicate that the result is undefined due to an unexpected error.
    print("An unexpected error occurred:", e)
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")
    print("Division operation attempted between", a, "and", b, "with result:", result)
    print("End of the program.")

