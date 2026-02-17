def sum(x, y):
    result = 0
    for i in range(x, y + 1):
        result += i
    
    return result

print(sum(1, 5))  # Output: 15 (1 + 2 + 3 + 4 + 5)