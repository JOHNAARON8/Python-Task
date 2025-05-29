import math

def findSquareRoot(Number):
    
    if Number  < 0:
        return "Invalid Input"
    elif Number== 0 or Number == 1:
        return Number
    else:
        result = math.sqrt(Number)
        return result
 
 
Number = int(input("Enter a number to find its square root: "))

result = findSquareRoot(Number)

print("The square root of", Number, "is:", result)

       
    
 

