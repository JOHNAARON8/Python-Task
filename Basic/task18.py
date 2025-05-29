string = str(input("Enter a string: "))

cnt = len(string)  

count = string.count('')
count -= 1  

print(f"The string contains {count} characters.")
print(f"The string contain {cnt} characters")