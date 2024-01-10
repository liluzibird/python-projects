# creating an empty list
list = []
total = 0.0;
  
# number of elements as input
laps = int(input("Enter number of laps: "))
  
# iterating till the range
for x in range(laps):
    time = float(input(f"Enter time for lap {x+1} (min.): "))

    total = total + time
    average = total/laps
  
    list.append(time) # adding the element

fastest = min(list)
slowest = max(list)
print(f"\nFastest time (min.): {fastest}")
print(f"Slowest time (min.): {slowest}")
print(f"Average time (min.): {average}")