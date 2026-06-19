def grade_to_point(grade):
    grades = {
        "A": 4.00,
        "A-": 3.75,
        "B+": 3.50,
        "B": 3.00,
        "B-": 2.75,
        "C+": 2.50,
        "C": 2.00,
        "C-": 1.75,
        "D": 1.50,
        "E": 1.20
    }
    return grades.get(grade.upper(), None)

def get_designation(avg):
    if avg >= 4.00:
        return "A"
    elif avg >= 3.75:
        return "A-"
    elif avg >= 3.50:
        return "B+"
    elif avg >= 3.00:
        return "B"
    elif avg >= 2.75:
        return "B-"
    elif avg >= 2.50:
        return "C+"
    elif avg >= 2.00:
        return "C"
    elif avg >= 1.75:
        return "C-"
    elif avg >= 1.50:
        return "D"
    else:
        return "E"

total = 0
count = 0

while True:
    grade = input("Enter Grade Category (Press Enter to Stop): ")

    if grade == "":
        break

    point = grade_to_point(grade)

    if point is not None:
        total += point
        count += 1
    else:
        print("Invalid grade category!")

if count > 0:
    average = total / count
    designation = get_designation(average)

    print(f"\nThe average grade is {average:.2f} with a designation of {designation}")
else:
    print("\nNo grades were entered.")