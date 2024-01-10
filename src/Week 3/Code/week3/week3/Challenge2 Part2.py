max = 100
num = float(input("Enter a number: "))
product = num * 10
print(f"Product: {product}")

while product < 100:
    product = product * 10
    print(f"Product: {product}")