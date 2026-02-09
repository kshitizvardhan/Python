# and: Both conditions must be True.
# or: At least one condition must be True.
# not: Reverses the result (True becomes False

age = int(input("Enter your age: "))
has_id = input("Do you have a voter ID? (yes/no): ").lower() == 'yes'

if age >= 18 and has_id:
    print("You are eligible to vote.")
elif age >= 18 and not has_id:
    print("You are eligible to vote, but you need a voter ID.")
else:
    print("You are not eligible to vote yet.")

# Example with 'or'
temperature = int(input("Enter the temperature in Celsius: "))  
is_raining = input("Is it raining? (yes/no): ").lower() == 'yes'
if temperature > 30 or is_raining:
    print("It's a good day to stay indoors.")
else:
    print("It's a nice day to go outside!")