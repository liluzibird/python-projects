import sqlite
import os

#os.remove("tutorial1.db")
con = sqlite3.connect("tutorial1.db")
cur = con.cursor()