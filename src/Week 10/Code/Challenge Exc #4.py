import sqlite3

con = sqlite3.connect("D:\\Skool\\SAC\\FALL 2022\\CMPR 114\\Week 10\\Code\\ContactsDB.db")
cur = con.cursor()#the cursor function allows to execute SQL statements
cur1 = con.cursor()
#like function that will search certain patterns of data
#display any names that ends with the letter s
cur.execute(''' Select * from employee where City = 'New York City' ''')
results = cur.fetchall()

cur1.execute(" Select * from employee where EmployeeID > 3;")
results1 = cur1.fetchall()

print ("EmployeeID Name Position Department City")
#for EmployeeID, Name, Position, Department, City in results:
#    print(f'{str(EmployeeID):9} {Name:13} {Position:8} {Department:12} {City:1}')

for EmployeeID, Name, Position, Department, City in results1:
    print(f'{str(EmployeeID):9} {Name:14} {Position:10} {Department:13} {City:1}')


con.commit()#saves all of the data

con.close()




