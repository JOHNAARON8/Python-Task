def checkNumber(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

r = int(input("Enter the range of the loops:"))

for i in range(r):
    number = int(input("Enter a number: "))
    result = checkNumber(number)
    print(f"The number {number} is {result}.")
 
