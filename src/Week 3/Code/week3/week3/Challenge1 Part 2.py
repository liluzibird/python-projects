
max = 5

total = 0.0

print('This program calculates the sum of')
print(f'{max} numbers you will enter.')

for counter in range(max): 
    number = int(input('Enter a number: '))
    total = total + number
    average = total/5

print(f'The total is {total}.\nThe average is {average}')