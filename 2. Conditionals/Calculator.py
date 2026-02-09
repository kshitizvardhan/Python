num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter an operator (+, -, *, /, %, //): ")

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    case "%":
        result = num1 % num2
    case "//":
        result = num1 // num2
    case _:
        result = "Error: Invalid operator!"
        
print("Result:", result)