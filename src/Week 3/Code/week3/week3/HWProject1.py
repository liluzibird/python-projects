
speed = int(input("Enter the speed (MPH): "))
miles = int(input("Enter the number of hours traveled: "))
distance = 0;


print("Hour\tDistance Traveled (Miles)")
print("------------------------------------")

for x in range(miles):
    distance = (x+1)*(speed)
    print(f"{x+1}\t{distance}")