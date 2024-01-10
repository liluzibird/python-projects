first_name1 = input("enter the firstname " "\n")
last_name1 = input("enter the lastname " + "\n")
hours1 = int(input("enter # of hours worked " + "\n"))
pay1 = int(input("enter your hourly pay " + "\n"))
total1 = hours1 * pay1

first_name2 = input("enter the firstname " "\n")
last_name2 = input("enter the lastname " + "\n")
hours2 = int(input("enter # of hours worked " + "\n"))
pay2 = int(input("enter your hourly pay " + "\n"))
total2 = hours2 * pay2

average_pay = (total1 + total2)/2

print(f"""{first_name1} {last_name1}'s total pay: {total1}
{first_name2} {last_name2}'s total pay: {total2}
Average pay: {average_pay}
""")