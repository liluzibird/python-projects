maxTemp = 102.5
temp1 = float(input("Enter the 1st temperature: "))
temp2 = float(input("Enter the 2nd temperature: "))
temp3 = float(input("Enter the 3rd temperature: "))
temp4 = float(input("Enter the 4th temperature: "))

while max(temp1, temp2, temp3, temp4) > maxTemp:
    print("Temp is over 102.5 F. Try again")
    temp1 = float(input("Enter the 1st temperature: "))
    temp2 = float(input("Enter the 2nd temperature: "))
    temp3 = float(input("Enter the 3rd temperature: "))
    temp4 = float(input("Enter the 4th temperature: "))
