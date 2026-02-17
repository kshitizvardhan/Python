# Python is different. It assumes "we are all consenting adults." 
# It does not strictly forbid access, but it uses Underscores (_) as warning signs 
# to tell other programmers: "Hey, don't touch this."

# There are three levels of access:

# 1. Public Members (No Underscores)
# Symbol: Just the name (e.g., self.name).
# Access: Can be accessed from anywhere (inside the class, outside the class, and by subclasses).

# 2. Protected Members (One Underscore _)
# Symbol: Single underscore prefix (e.g., self._money).
# Access: Technically accessible from anywhere, but conceptually meant only for the class itself and its subclasses (children).
# Note: Python does not stop you from accessing this, but your IDE (code editor) might give you a warning.

# 3. Private Members (Two Underscores __)
# Symbol: Double underscore prefix (e.g., self.__password).
# Access: Cannot be accessed directly from outside the class. 
# Python actively hides these variables using a technique called Name Mangling.
# Name Mangling: Python changes the name of the variable to include the class name, making it harder to access from outside.
# For example, if you have a class named User and a private variable __password, Python will internally rename it to _User__password.
# This means you cannot access it using user.__password, but you can access it using user._User__password (though this is not recommended).


# Example of Access Modifiers in a Class

class BankAccount:

    def __init__(self):
        self.accountHolder = "Kshitiz"     # Public member
        self._balance = 1000                # Protected member
        self.__pin = "2303"                 # Private member


    def publicFunction(self):
        print(f"Account Holder: {self.accountHolder}")  # Accessing public member
        print(f"Balance: {self._balance}")              # Accessing protected member
        print(f"PIN: {self.__pin}")                     # Accessing private member

    def _protectedFunction(self):
        print("This is a protected function.")  

    def __privateFunction(self):
        print("This is a private function.")

    
    


# Creating an instance of BankAccount
account = BankAccount()
# Accessing members
# print(account.accountHolder)  # Output: Kshitiz (Public member)
# print(account._balance)     # This will raise an AttributeError (Protected member)
# print(account.__pin)       # This will raise an AttributeError (Private member)


# Calling the displayInfo method to show all members from within the class
account.publicFunction()

# Demonstrating name mangling for private members
# Even though __pin is private, Python internally renames it to _BankAccount__pin
# This is not recommended, but it shows how name mangling works
print(f"Accessing private member through name mangling: {account._BankAccount__pin}")

# Accessing private function through name mangling
account._BankAccount__privateFunction()  # This will work, but it's not recommended to access private members or functions from outside the class.
account._protectedFunction()  # This will work, but it's not recommended to access protected members or functions from outside the class.


# Summary:
# - Public members (no underscore): Accessible from anywhere
# - Protected members (single underscore): Meant for class and subclasses only
# - Private members (double underscore): Hidden through name mangling, not directly accessible

# Best Practices:
# 1. Use public members for data that should be accessible to everyone
# 2. Use protected members for internal implementation details that subclasses might need
# 3. Use private members for sensitive data that should never be accessed directly from outside
# 4. Always use proper getter/setter methods instead of accessing protected/private members directly