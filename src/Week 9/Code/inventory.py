import sqlite3
import os #for directory like folders files on the OS

os.remove("tutorial1.db") #removes database
                 # con is variable name and following connects to that database
con = sqlite3.connect("tutorial1.db") #this line creates  tutorial1 database
con1=sqlite3.connect("C:\\Users\\tanny\\Documents\\CMPR 114 PYTHON\\M9\\CompanyDB.db") #connects to db we created in sqllite3 app
cur = con.cursor() # connects to the database
                                                            #the cur.excute allows us to execute queries
cur.execute('''Create Table Inventory( 
ItemID INTEGER Primary Key,
ItemName TEXT,
Price REAL)''') 
#it has 3 apostrophes '''

con.commit #this writes the table into the Hard Disk

cur.execute(''' Insert into Inventory(ItemID, ItemName,Price)
values
(100, 'Screw Driver', 4.99) ''')

cur.execute(''' Insert into Inventory(ItemID, ItemName,Price)
values
(200, 'Hammer', 5.99) ''')

cur.execute(''' Insert into Inventory(ItemID, ItemName,Price)
values
(300, 'Nails', 1.99) ''')
                                                                         #retrieves the two rows in line 25
cur.execute(''' Select * from Inventory ''')
#result is a variable used to contain the 2 rows
results = cur.fetchall() #contains the two rows in the results variable

for row in results: #loops through results that contain the rows and prints them out
    print(f'{row[0] :0} {row[1] :5} {row[2] :5} ') 
    #the formating spaces matter in line 30, it didnt run with spaces in {row[0]:5}
    # the first number is how many spaces you want inbetween the output 0 starts on far left row 2 starts 5 spaces after row 3  also 5 spaces after
    #the second number is the row (first row starts at index 0 )  (second row of hammer is index 1)

con.close()