def convertCel (celcius):
    return (celcius * 9/5) + 32

celsius = float(input("Please enter the temperature in Celsius: "))

result = convertCel(celsius)

print(f"The temperature in Fahrenheit is: {result:.2f}°F")