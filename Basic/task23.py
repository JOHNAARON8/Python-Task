#dectionary 

dectionary = {
   "John": 80,
    "Emma": 90,
    "Max": 78,
    "Sophia": 95,
    "Olivia": 88  
}

check= input("Enter the name of the student: ")

if check in dectionary:
    print(f"\nThe score of {check} is: {dectionary[check]}\n")
    
else:
    print(f"\nThe student {check} is not present in the dictionary.\n")