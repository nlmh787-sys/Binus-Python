repeat = "Y"

while repeat.upper() == "Y":
    number = int(input("Enter any number: "))

    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")

    repeat = input("Do you want to repeat? (Y/N): ")

print("\nProgram Stops")