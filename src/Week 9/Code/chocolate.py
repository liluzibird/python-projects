#this is to get from and existing db in sqlite

import sqlite3
import os

#to remove db
#os.remove("D:\\Skool\\SAC\\FALL 2022\\CMPR 114\\Week 9\\Code\\HWCHocolateDB.db")

#to create/connect to  db?
variable = sqlite3.connect("D:\\Skool\\SAC\\FALL 2022\\CMPR 114\\Week 9\\Code\\HWCHocolateDB.db")

#connect to db
curcur=variable.cursor()

#write table to hard disk
variable.commit

#retrieves all rows
curcur.execute(''' Select * from Products ''')

#store the rows in the variable results
results = curcur.fetchall()

print("The Products Table")

#for to to get and print the rows , row for each 
for row in results:
    if (row[2] > 8): #if price is greater than $8
    #if (row[0] == "Bolivian Dark"): #if description is Bolivian Dark
    #if (row[1] == "17-003"): #if ProdNum is 17-003
        print(f'{row[0] :0} {row[1] :5} {row[2] :2}')

