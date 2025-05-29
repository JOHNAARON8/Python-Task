def checkNumber(num):
    if num < 0:
        return "The number is negative"
    elif num == 0:
        return "The number is zero"
    else:
        return "The number is positive"


r = int(input("Enter the range of the loops: "))
for i in range(r):
    number = int(input("Enter a number: "))
    result = checkNumber(number)
    print(f"{result}.")
 