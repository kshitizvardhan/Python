# In many languages (like C++ or Java), you use curly brackets { } to group code. 

# In Python, we use Indentation (spaces).

# A colon : tells Python "Okay, the condition is done, here is what comes next."
# The lines following the colon must be indented (usually 4 spaces or 1 tab).

age = int(input("Enter your age: "))

if age > 18:
    print("Yes, you are eligible.")
    print("You can vote now.")

print("This line is always executed.") # This line is outside the if block, as it is not indented