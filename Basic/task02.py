def AddNumber(num1 , num2):
    
    sum = num1 + num2
    
    return sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = AddNumber(num1, num2)

print("The sum of", num1, "and", num2, "is:", result)