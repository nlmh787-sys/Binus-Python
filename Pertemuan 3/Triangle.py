side_a = float(input("Enter Side A: "))
side_b = float(input("Enter Side B: "))
side_c = float(input("Enter Side C: "))

if (side_a + side_b <= side_c or
    side_a + side_c <= side_b or
    side_b + side_c <= side_a):
    triangle_type = "Not a Triangle"

else:
    sides = sorted([side_a, side_b, side_c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        triangle_type = "Right-angled Triangle"

    elif side_a == side_b == side_c:
        triangle_type = "Equilateral Triangle"

    elif side_a == side_b or side_a == side_c or side_b == side_c:
        triangle_type = "Isosceles Triangle"

    else:
        triangle_type = "Scalene Triangle"

print("Triangle Type:", triangle_type)