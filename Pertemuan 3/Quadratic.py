import math

a = float(input("Enter value A: "))
b = float(input("Enter value B: "))
c = float(input("Enter value C: "))

if a == 0:
    print("It is not a quadratic equation")

else:
    discriminant = b**2 - 4*a*c

    print(f"\nQuadratic Equation: {a}x² + {b}x + {c} = 0")
    print("Discriminant =", discriminant)

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)

        print("It has distinct roots")
        print("Root x1 =", x1)
        print("Root x2 =", x2)

    elif discriminant == 0:
        x = -b / (2*a)

        print("It has a double root")
        print("Root =", x)

    else:
        print("It has imaginary roots")
        print("x1 = (-b + √D) / (2a)")
        print("x2 = (-b - √D) / (2a)")