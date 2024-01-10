import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

win = tk.Tk()
win.geometry("350x250")
win.title("Student Information")
lblID = tk.Label(win, text = "Enter the student ID: ").grid(column = 0, row = 0)
lblLastname = tk.Label(win, text = "Enter the last name: ").grid(column = 0, row = 1)
lblFirstname = tk.Label(win, text = "Enter the first name: ").grid(column = 0, row = 2)
lblAddress = tk.Label(win, text = "Enter the address: ").grid(column = 0, row = 3)
lblCity = tk.Label(win, text = "Enter the city: ").grid(column = 0, row = 4)
lblState = tk.Label(win, text = "Enter the state: ").grid(column = 0, row = 5)
lblZipCode = tk.Label(win, text = "Enter the zip code: ").grid(column = 0, row = 6)
lblGender = tk.Label(win, text = "Enter the Gender: ").grid(column = 0, row = 7)
lblAge = tk.Label(win, text = "Enter the age: ").grid(column = 0, row = 8)

def write():
	text_file = open("E:\\Skool\\SAC\\FALL 2022\\CMPR 114\\Final\\Code\\Students.txt", "a")
	content = text_file.write("Confirmation: " + "\n" + ID.get() + "\n" + LN.get() + ", " + FN.get() + "\n"
		+ A.get() + "\n" + C.get() + "\n" + S.get() + "\n" + ZC.get() + "\n" + G.get() + "\n"
		+ Age.get() + "\n---------------------------------------------------\n")
	text_file.close()
	messagebox.showinfo("Information", "Data Recorded")

def quit():
	messagebox.showinfo("Information","Data Recorded")
	win.destroy()

def submit():
	messagebox.showinfo("Information", "Entered: " + "\n" + ID.get() + "\n" + LN.get() + ", " + FN.get() + "\n"
		+ A.get() + "\n" + C.get() + "\n" + S.get() + "\n" + ZC.get() + "\n" + G.get() + "\n"
		+ Age.get())

ID = tk.StringVar()
txtID = tk.Entry(win, width = 24, textvariable = ID).grid(column = 1, row = 0)
LN = tk.StringVar()
txtLastname = tk.Entry(win, width = 24, textvariable = LN).grid(column = 1, row = 1)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width = 24, textvariable = FN).grid(column = 1, row = 2)
A = tk.StringVar()
txtAddress = tk.Entry(win, width = 24, textvariable = A).grid(column = 1, row = 3)
C = tk.StringVar()
txtCity = tk.Entry(win, width = 24, textvariable = C).grid(column = 1, row = 4)
S = tk.StringVar()
txtState = tk.Entry(win, width = 24, textvariable = S).grid(column = 1, row = 5)
ZC = tk.StringVar()
txtZipCode = tk.Entry(win, width = 24, textvariable = ZC).grid(column = 1, row = 6)
G = tk.StringVar()
txtGender = tk.Entry(win, width = 24, textvariable = G).grid(column = 1, row = 7)
Age = tk.StringVar()
txtAge = tk.Entry(win, width = 24, textvariable = Age).grid(column = 1, row = 8)

btnSubmit = tk.Button(win, text = "Submit", command = submit).grid(column = 0, row = 10)

btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 1, row = 10)


btnWrite = tk.Button(win, text = "Transfer", command = write).grid(column = 2, row = 10)

win.mainloop()
submit()

con = sqlite3.connect("StudentsDB.db")
cur = con.cursor()

cur.execute('''CREATE TABLE Students
(StudentID TEXT PRIMARY KEY NOT NULL,
Lastname TEXT NOT NULL,
Firstname TEXT NOT NULL,
Address TEXT NOT NULL,
City TEXT NOT NULL,
State TEXT NOT NULL,
Zipcode TEXT NOT NULL,
Gender TEXT NOT NULL,
Age TEXT NOT NULL)''')

con.commit()

cur.execute('''INSERT INTO Students 
(StudentID, Lastname, Firstname, Address, City, State, Zipcode, Gender, Age)
VALUES
("100","100","100","100","100","100","100","100","100")
#("ID.get()", "LN.get()", "FN.get()", "A.get()", "C.get()", "S.get()", "ZC.get()", "G.get()", "Age.get()" )''')

cur.execute('''Select * from Students''')
results = cur.fetchall()

for row in results:
	print(f'{row[0]:1} {row[1]:1} {row[2]:1} {row[3]:1} {row[4]:1} {row[5]:1} {row[6]:1} {row[7]:1} {row[8]:1} ')

con.close()