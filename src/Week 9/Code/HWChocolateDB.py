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
print('*' *40)

#for to to get and print the rows , row for each 
for row in results:
    print(f'{row[0] :0} {row[1] :5} {row[2] :2} {row[3] :2} {row[4] :2}') 

#for warehouse table
curcur.execute(''' Select * from Warehouse ''') #getting all from warehourse table
resultsWarehouse = curcur.fetchall()  #storeing it in resulsWarehouse variable
print(" ")
print("The Warehouse Table")
print('*' *40)
for row in resultsWarehouse :  #using for loop to print all the rows
    print(f'{row[0] :0} {row[1] :5} {row[2] :2}')  #theres only 3 of them in warehouse table


#remember to join both tables in sqlite db using the join statement

curcur.execute(''' Select Products.ProductId, Description,UnitCost, RetailPrice, UnitsOnHand,
StorageLocation
from Products, Warehouse
where Products.ProductId=Warehouse.ProductId''')

resultsCombined = curcur.fetchall()
#labels
print(" ")
print("The Tables Combined")
print('*' *40)
#for loop to print out the table, remember to add a 6th items since there are 6 in line 42-43
for row in resultsCombined:
    print(f'{row[0] :0} {row[1] :5} {row[2] :2} {row[3] :2} {row[4] :2} {row[5] :2}') 

variable.close()