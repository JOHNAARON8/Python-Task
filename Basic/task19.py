
fruit = []

r = int(input("Enter how many fruit you want to add in a list: "))

for i in range(r):
    fruit.append(input("Enter a fruit: "))
    

print("The list of fruits is:")
for i in range(len(fruit)):
    print(i+1,".",fruit[i])
