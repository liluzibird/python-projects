
max = 5
days = 1
total = 0

for days in range(max): 
    bugs = int(input("Enter number of bugs collected: "))
    total = total + bugs 
print(f"Total number of bugs collected: {total}")