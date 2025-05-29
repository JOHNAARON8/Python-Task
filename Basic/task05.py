def calculateArea(width, height):
    return (width * height)


w = float(input("Enter the width of the rectangle: "))
h = float(input("Enter the height of the rectangle: "))

result = calculateArea(w, h)

print(f"The area of the rectangle is: {result:.2f} square units")