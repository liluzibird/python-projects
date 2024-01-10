
pocketNum = int(input("Enter a pocket number: "))

if pocketNum == 0:
    "Pocket is green"
else:
    if 1 <= pocketNum <= 10 and (pocketNum % 1) == 0:
        print("Pocket is red")
    elif (pocketNum % 2) == 0:
        print("Pocket is black")
    else:
        if 11 <= pocketNum <= 18 and (pocketNum % 1) == 0:
            print("Pocket is black")
        elif (pocketNum % 2) == 0:
            print("Pocket is red")
        else:
            if 19 <= pocketNum <= 28 and (pocketNum % 1) == 0:
                print("Pocket is red")
            elif (pocketNum % 2) == 0:
                print("Pocket is black")
            else:
                if 29 <= pocketNum <= 36 and (pocketNum % 1) == 0:
                    print("Pocket is black")
                elif (pocketNum % 2) == 0:
                    print("Pocket is red")
                else: print("Invalid input. Please try again.")