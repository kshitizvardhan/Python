print("------Club Bouncer Bot------")

age = int(input("How old are you?: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == 'yes'

if age >= 21 and has_id:
    print("Welcome to the club! You may enter.")
else:
    print("Sorry, you cannot enter the club.")