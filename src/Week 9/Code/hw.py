#homework module 9

#import libararies
import sqlite3
import os

#connect to db in sqlite
con= sqlite3.connect("C:\\Users\\tanny\\Documents\\CMPR 114 PYTHON\\M9\\Coffee.db")
cur = con.cursor()
con.commit
#excute sql statment and fetch table
cur.execute(''' Select * from coffee ''')
#store results in results variable
results = cur.fetchall()
#print results
for row in results:
    print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2}')

#Print where coffee price is greater than $8.00
print("")
print("Price greater than $8.00")
print("*" *20)
cur.execute(''' Select * from Coffee where Price > 8.00; ''')
#store results in results variable
results2 = cur.fetchall()
#print results
for row in results2:
    print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2}')

#extract only Bolivian Dark description
print("")
print("Only Bolivian Dark")
print("*" *20)
cur.execute(''' Select * from Coffee where Description = 'Bolivian Dark' ''')
results3 = cur.fetchall()
for row in results3:
    print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2}')

#extract only ProdNum is 17-003 
print("")
print("Only ProdNum is 17-003 ")
print("*" *20)
cur.execute(''' Select * from Coffee where ProdNum = '17-003' ''')
results4 = cur.fetchall()
for row in results4:
    print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2}')

con.close()