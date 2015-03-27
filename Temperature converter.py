#  Name:Brian
#  Program Name:  Temperature
#  Description of what code does:
#Converts the temperature in Fahrenheit, to the temperature in Celsius

celsius = float(input("Enter a temperature in celsius"))
print("The celsius temperature is",celsius,"so the fahrenheit temperature is ",((9.0 / 5.0) * celsius + 32.0))
fahrenheit = float(input("Enter a temperature in fahrenheit"))
print("The fahrenheit temperature is",fahrenheit,"so the celsius temperature is ",((5.0 * (fahrenheit - 32.0)) / 9.0))
