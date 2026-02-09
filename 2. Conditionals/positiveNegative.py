num = int(input("Enter a number: "))

if num == 0: 
    print("Zero is neither Positive nor Negative") 
    exit()

if num > 0:
    print(str(num) + " is Positive")
else:
    print(str(num) + " is Negative.")