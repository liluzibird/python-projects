import sqlite3
import os

#connect to db in sqlite
con= sqlite3.connect("D://Skool//SAC//FALL 2022//CMPR 114//Quiz 2//Q2DB.db")
cur = con.cursor()

#excute sql statment and fetch table
#cur.execute(''' Select * from Warehouse ''')
#store results in results variable
cur.execute('''Select Location, Bin, Category, QTY, Region from Warehouse, Region
	Where Warehouse.WarehouseID = Region.WarehouseID''')
results = cur.fetchall()

for row in results:
	print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2} {row[4] :2}')


#print the entire table
# print("Print entire table: ")
# for row in results:
#    print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2} {row[4] :2}')

#print the sum of QTY column
# print("Total of QTY: ")
# cur.execute(''' Select sum(QTY) from Warehouse''')
# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0}')

#print the sum of QTY column


# cur.execute(''' Select Location from Warehouse''')
# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0}')

# cur.execute(''' Select Category from Warehouse''')
# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0}')

# cur.execute(''' Select Bin from Warehouse''')
# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0}')

# cur.execute(''' Select QTY from Warehouse''')
# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0}')

# cur.execute(''' Select Region from Region''')
# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0}')



# print("Everything in category ends with s: ")
# cur.execute(''' Select * from Warehouse where Category like '%s' ''')

# results = cur.fetchall()
# #print results
# for row in results:
#     print(f'{row[0] :0} {row[1] :2} {row[2] :2} {row[3] :2} {row[4] :2}')


