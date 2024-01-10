salary = 0
salary1 = 70000
salary2 = 80000
salary3 = 90000

sales = float(input("Enter the sales: "))
if 50000 <= sales < 70000:
	salary = salary1 * 1.1
	print("Salary: $",format(salary,",.2f"),"(10%)")
elif 70000 <= sales <= 90000:
	salary = salary2 * 1.2
	print("Salary: $",format(salary,",.2f"),"(20%)")
elif 90000 <= sales <= 100000:
	salary = salary3 * 1.3
	print("Salary: $",format(salary,",.2f"),"(30%)")
else:
	print("Invalid input. Please try again")
