#removed and add item from the list

myList = []

r = int(input("Enter how many items you want to add in a list: "))

for i in range(r):
    myList.append(input("Enter an item: "))

print(f"\nThe list of items is: {myList}")


option = str(input("\nEnter yes if you want to removed an item from the list: "))

if option.lower() == 'yes':
    item_removed= input("\nEnter the item you want to remove: ")
    
    myList.remove(item_removed)
    print(f"\nThe updated list of items is: {myList}")
else:
    print("\nNo item removed from the list.")