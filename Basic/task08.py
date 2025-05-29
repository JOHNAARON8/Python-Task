def findFactorial(n):
    if n < 0:
        return "Not allowes negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        
        fac = 1     
        for i in range(1, n+1):
            fac *= i
        return fac
        
n = int(input("Enter a number to find the factorial: "))

results = findFactorial(n)

print(f"The factorial of {n} is: {results}")
