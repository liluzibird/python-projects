tests = 4
testNum = 0
total = 0.0

for testNum in range(tests):
	print("Test number", testNum +1)
	score = float(input(": "))
	total += score

average = total / tests
while average > 100:
	print("Average cannot be over 100. Please try again.")
	break
print("The average for the scores is: ", average)

if 90 <= average <= 100:
	print("You earned an A!")
elif 80 <= average < 90:
	print("You earned an B!")
elif 70 <= average < 80:
	print("You earned an C!")
elif 60 <= average < 70:
	print("You earned an D!")
elif 60 > average:
	print("You earned an F!")
else: print("Invalid input. Please try again")