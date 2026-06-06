print("Temperature Conversion Menu")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Select menu (1-6): "))
temperature = float(input("Enter temperature value: "))

# Process and Output
if choice == 1:
    result = (temperature * 9/5) + 32
    print("Result:", result, "°F")

elif choice == 2:
    result = temperature + 273.15
    print("Result:", result, "K")

elif choice == 3:
    result = (temperature - 32) * 5/9
    print("Result:", result, "°C")

elif choice == 4:
    result = (temperature - 32) * 5/9 + 273.15
    print("Result:", result, "K")

elif choice == 5:
    result = temperature - 273.15
    print("Result:", result, "°C")

elif choice == 6:
    result = (temperature - 273.15) * 9/5 + 32
    print("Result:", result, "°F")

else:
    print("Invalid menu option.")