score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Good job!")
elif score >= 70:
    print("Grade: C")
    print("You passed.")
elif score >= 60:
    print("Grade: D")
    print("Passed, but needs improvement.")
else:
    print("Failed Grade: F, better luck next time!")