def print_profile():
    print("Natan")
    print("Jakarta")
    print("-" * 40)
    
# Functions with two parameters and default values
def add(a=0, b=0):
    return a + b

def subtract(a=0, b=0):
    return a - b

def multiply(a=1, b=1):
    return a * b

def divide(a=1, b=1):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a=0, b=1):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


# Main program
print_profile()

while True:
    menu = input("Enter Menu (+|-|/|*|%|stop): ").strip()

    if menu.lower() == "stop":
        print("Program stopped.")
        break

    if menu not in ["+", "-", "*", "/", "%"]:
        print("Invalid menu choice. Please try again.\n")
        continue

    value1 = float(input("Enter Value 1: "))
    value2 = float(input("Enter Value 2: "))

    if menu == "+":
        result = add(value1, value2)
        print(f"The result of addition {value1} + {value2} is {result}")

    elif menu == "-":
        result = subtract(value1, value2)
        print(f"The result of subtraction {value1} - {value2} is {result}")

    elif menu == "*":
        result = multiply(value1, value2)
        print(f"The result of multiplication {value1} * {value2} is {result}")

    elif menu == "/":
        result = divide(value1, value2)
        print(f"The result of division {value1} / {value2} is {result}")

    elif menu == "%":
        result = modulus(value1, value2)
        print(f"The result of modulus {value1} % {value2} is {result}")

    print()