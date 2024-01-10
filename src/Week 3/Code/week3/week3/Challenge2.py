

loop = 1

while loop <= 4:
    sales = float(input("Enter the amount of sales: "))
    commRate = float(input("Enter the commission rate: "))
    loop = loop + 1
commission = sales * commRate
print(f'The commission is ${commission:,.2f}.')
