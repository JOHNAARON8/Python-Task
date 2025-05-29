def displayBack(n):
    for i in range(n, 0, -1):
        print(f"Number: {i}")
        
n = int(input("Enter a number to display it in reverse order: "))

print(f"The reverse order of the number")
displayBack(n)
