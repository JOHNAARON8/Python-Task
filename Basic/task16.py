checker = set("@#$%^&*()_+[]{}|;':\",.<>?/~`")

string = str(input("Enter a string: "))

if any(char in checker for char in string):
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")