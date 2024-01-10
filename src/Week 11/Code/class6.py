import class5

def main():
	start_bal = float(input("Enter the starting balance"))

	savings = class5.BankAccount(start_bal)

	pay = float(input("Enter the amount you were paid this week "))
	print("Will deposit the pay into the account ")

	savings.deposit(pay)
	print("Your account balance is $", format(savings.get_balance(), ",.2f"))

	cash = float(input("Enter the amount to withdrawal "))
	print("Will withdrawal that amount from your account ")

	savings.withdraw(cash)

	print("Your account balance is $", format(savings.get_balance(), ",.2f"))
main()	