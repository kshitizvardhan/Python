age = int(input("Enter your age: "))

if age >= 18:
    print("Congratulations!")
    print("You are eligible to vote.")
    print("You are an adult.\nVoter ID can be applied.")
else:
    print("Sorry!")
    print("You are not eligible to vote yet.")
    print("You are a minor.")
    print("Please apply again in " + str(18-age) + " years.")

print("This line is always executed.") # This line is outside the if-else block, as it is not indented