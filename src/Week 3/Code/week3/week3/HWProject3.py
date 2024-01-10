list = []
while True:
    x = int(input("Enter a series of positive numbers. To end the series, enter a negative number: "))
    if x > 0:
        list.append(x)
    if x < 0:
        print(f"Series of numbers entered: {list}")
        break