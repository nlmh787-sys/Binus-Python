age = int(input("Enter age: "))
if ( age < 0 ):
    print("Too low")
if ( ( age >= 0) and ( age <= 1) ):
    print ("Baby")
if ( ( age >= 2) and ( age <= 3) ):
    print ("Toddler")
if ( ( age >= 4) and ( age <= 5) ):
    print ("Preschooler")
if ( ( age >= 6) and ( age <= 12) ):
    print ("Child")
if ( ( age >= 13) and ( age <= 17) ):
    print ("Teenager")
if ( ( age >= 18) and ( age <= 21) ):
    print ("Young Adult")
if ( ( age >= 22) and ( age <= 30) ):
    print ("Pre-adult")
if ( ( age >= 31) and ( age <= 50) ):
    print ("Adult")
if ( ( age >= 51) and ( age <= 70) ):
    print ("Pre-elderly")
if ( age > 70 ):
    print ("Elderly")