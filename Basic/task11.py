def getSum(n):
    if n < 0:
        return "The negative number is not allowed"
    elif n == 0:
        return 0
    else:
        sum = 0
        for i in range(1, n+1, 1):
            sum += i
        return sum
            
 
n = int(input("Enter a number to find the sum all the number: "))
result = getSum(n)

print(f"The sum of the {n} is: {result}")