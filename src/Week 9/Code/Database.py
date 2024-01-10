import sqlite3
import os

os.remove("CustomersDB.db")
con = sqlite3.connect("CustomersDB.db")
cur = con.cursor()

cur.execute('''CREATE TABLE Customers
CustomerID TEXT PRIMARY KEY NOT NULL,
Lastname TEXT NOT NULL,
Firstname TEXT NOT NULL,
Address TEXT NOT NULL,
State TEXT NOT NULL,
Zipcode TEXT NOT NULL)''')

cur.execute('''CREATE TABLE Orders
(OrderID TEXT PRIMARY KEY NOT NULL,
Product TEXT NOT NULL,
Price TEXT NOT NULL,
Constraint CustomerID_FK Foreign Key (CustomerID) references Customers (CustomerID))''')

con.commit()

cur.execute('''INSERT INTO Customers
(CustomerID, Lastname, Firstname, Address, City, State, Zipcode)
VALUES
("A1" , "Doe", "Jill", "123 Street", "Santa Ana", "CA", "11111")''')

cur.execute('''INSERT INTO Customers
(CustomerID, Lastname, Firstname, Address, City, State, Zipcode)
VALUES
("A2" , "Cantor", "Bill", "456 Street", "Santa Ana", "CA", "11111")''')

cur.execute('''INSERT INTO Orders
(OrderID, CustomerID, Product, Price)
VALUES
("100", "A1", "Laptop", 599.99)''')

cur.execute('''Select Customers.CustomerID, Lastname, Firstname, Addres,, City, State, Zipcode, OrderID, Product, Price
	from Customers, Orders
	Where Customers.CustomerID = Orders.CustomerID''')
	results = cur.fetchall()

	for row in results:
		print(f'{row[0]:1} {row[1]:1} {row[2]:1} {row[3]:1} {row[4]:1} {row[5]:1} {row[6]:1} {row[7]:1} {row[8]:1} {row[9]:1}')
		con.close()