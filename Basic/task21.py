#Find the largest number in the list

myList = []

r = int(input("Enter how many numbers you want to add in a list: "))

for i in range(r):
    myList.append(int(input("Enter a number: ")))
    
print(f"\nAll the number in the list is: {myList}")

largest = max(myList)

print(f"\nThe largest number in the list is: {largest}\n")