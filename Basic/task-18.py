vowel = ['a', 'e', 'i', 'o', 'u']

string = str(input("Enter a string: "))

count= 0

if string:
    for i in string:
        if i.lower() in vowel:
            count += 1
            
print(f"The string contains {count} vowels.")

