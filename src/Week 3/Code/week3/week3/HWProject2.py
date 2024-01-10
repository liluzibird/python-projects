
years = int(input("Enter the number of years: "))
months = 12;
total = 0.0;

for x in range(years):
    for y in range(months):
        rainfall = float(input(f"Enter the rainfall (in.) for year {x+1}, month {y+1}: "))
        total = total + rainfall
        average = (total)/(years*months)
months = years * months
print(f"Number of months: {months}")
print(f"Total rainfall (in.): {total}")
print(f"Average rainfall (in.): {average}")