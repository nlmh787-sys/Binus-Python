repeat = "Y"

while repeat.upper() == "Y":
    side_a = float(input("Enter Side A: "))
    side_b = float(input("Enter Side B: "))
    side_c = float(input("Enter Side C: "))

    if side_a == side_b == side_c:
        print("\nIt is an Equilateral Triangle")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("\nIt is an Isosceles Triangle")
    else:
        print("\nIt is a Scalene Triangle")

    repeat = input("\nDo you want to repeat? (Y/N): ")

print("\nProgram Stops")