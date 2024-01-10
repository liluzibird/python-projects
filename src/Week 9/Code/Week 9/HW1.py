import sqlite3
import os

os.remove("tutorial1.db")
con = sqlite3.connect("tutorial1.db") #Creates the DB
cur = con.cursor() #connect to the DB

cur.execute('''Create Table Inventory(
Primary key,
Description TEXT,
ProductNum INTEGER,
Price REAL,
RetailPrice REAL)''')