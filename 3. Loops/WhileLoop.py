# Use a while loop when you want to repeat something as long as a specific condition is True. 
# You don't necessarily know how many times it will run beforehand.

# Caution: You must ensure the condition eventually becomes False, otherwise you create an Infinite Loop (a loop that never stops and freezes your program).


count = 0

while count < 5:
    print("Count is:", count)
    count += 1  # Increment count by 1, important to avoid infinite loop

print("Loop ended. Final count is:", count)