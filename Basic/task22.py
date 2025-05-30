myList = []

r = int(input("Enter how many items you want to add in a list: "))

for i in range(r):
    myList.append(input("Enter an item: "))

check = input("\nEnter an item you want to check in the list: ")

if check in myList:
    print(f"\nThe item '{check}' is present in the list.")
else:
    print(f"\nThe item '{check}' is not present in the list.")