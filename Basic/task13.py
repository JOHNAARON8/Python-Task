

n1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
n2 = int(input("Enter second number: "))

match operator:
    case '+':
        result = n1 + n2
    case '-':
        result = n1 - n2
    case '*':
        result = n1 * n2
    case '/':
        if n2 == 0:
            result = "Error: Division by zero"
        else:
            result = n1 / n2

print(f"{n1} {operator} {n2} = {result}")
    
