import sqlite3

con = sqlite3.connect("C:\\Users\\a206\\Desktop\\ContactsDB.db")
cur = con.cursor()#the cursor function allows to execute SQL statements
cur1 = con.cursor()
#like function that will search certain patterns of data
#display any names that ends with the letter s
cur.execute(''' Insert into Company (ID, Name, age, Address, salary)
values(5,'Jason',45,'CA',60000) ''')
results = cur.fetchall()

print ("enter new data")

cur1.execute(''' Select * from Audit ''')

print('ID  Entry Date ')
for id_, name, phone, address, city, state, _ in results:
    print(f'{id:9} {ENTRY_DATE:14}')

con.commit()#saves all of the data

con.close()




