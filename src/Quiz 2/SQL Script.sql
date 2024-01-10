import sqlite3
import os

con = sqlite3.connect("Q2DB.db")
cur = con.cursor()

cur.execute('''CREATE TABLE Warehouse
(WarehouseID INTEGER PRIMARY KEY NOT NULL,
Location TEXT,
Bin INTEGER,
Category TEXT,
QTY INTEGER)''')

con.commit()

cur.execute('''INSERT INTO Warehouse
(WarehouseID, Location, Bin, Category, QTY)
VALUES
(100, "SE", 1211, "Electronics", 1000))

cur.execute('''INSERT INTO Warehouse
(WarehouseID, Location, Bin, Category, QTY)
VALUES
(200, "NE", 3232, "Household Products", 2000))

cur.execute('''INSERT INTO Warehouse
(WarehouseID, Location, Bin, Category, QTY)
VALUES
(300, "W", 4343, "Food Items", 3000))

cur.execute('''INSERT INTO Warehouse
(WarehouseID, Location, Bin, Category, QTY)
VALUES
(400, "N", 4322, "Misc.", 4000))

cur.execute('''INSERT INTO Warehouse
(WarehouseID, Location, Bin, Category, QTY)
VALUES
(500, "S", 4342, "Clothing", 5000))

cur.execute('''INSERT INTO Warehouse
(WarehouseID, Location, Bin, Category, QTY)
VALUES
(600, "E", 1121, "Footwear", 6000))

