
t1 = float(input("Enter first test score: "))
t2 = float(input("Enter second test score: "))
t3 = float(input("Enter third test score: "))

average = (t1 + t2 + t3)/3

if average >100:
    print("The average cannot be over 100, try again")
else:
    print('The average score is: ' , round(average))

if average >=90 and average <=100:
    print('letter grade A', round(average))
elif average >=80 and average <89:
    print('letter grade B' ,round(average))
elif average >=70 and average <79:
    print('letter grade C' ,round(average))
elif average >=60 and average <69:
    print('letter grade D' ,round(average))
else:
    print('letter grade F', round(average))

#writes to the text file
f = open("Grades.txt", "a")
f.write('The average score is ' + str(round(average))+ "\n")
f.close()

#reads from the text file
f = open("Grades.txt", "r")
print(f.read())

#writes to the text file
f = open("D:\CMPR 114\Week 2\Code\Grades.txt", "a")
f.write('The average score is ' + str(round(average))+ "\n")
f.close

#reads from the text file
f = open("Grades.txt", "r")
print(f.read())