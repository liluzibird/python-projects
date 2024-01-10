
test1 = float(input("Enter the first test score: "))
if 0 <= test1 <= 25:
    test2 = float(input("Enter the second test score: "))
else:
    print("Invalid input. Please try again.")
if 0 <= test2 <= 25:
    exam = float(input("Enter the main exam score: "))
else:
    print("Invalid input. Please try again.")
if 0 <= exam <= 50:
    grade = test1 + test2 + exam;
else:
    print("Invalid input. Please try again.")

if grade < 50:
    print("You failed!")
elif exam < 25:
    print("You failed!")
elif grade > 80:
    print("Passed With Distinction!")
elif 60 < exam < 80:
    print("You Passed!")
else:
    print("Invalid input. Please try again.")