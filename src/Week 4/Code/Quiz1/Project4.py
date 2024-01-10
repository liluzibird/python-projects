sales = float(input("Enter the sales: "))
if 50000 <= sales <= 60000:
	print("Commission: 10%")
elif 70000 <= sales <= 80000:
	print("Commission: 20%")
elif 90000 <= sales <= 100000:
	print("Commission: 30%")
else:
	print("Invalid input. Please try again")
