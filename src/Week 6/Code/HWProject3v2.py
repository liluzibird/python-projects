import tkinter as tk
from tkinter import messagebox

def write():
    total = 0
    file = open("sumOfNumbers.txt", 'w')
    for i in range (100, 1001,100):  #first number is where to start, then the number how many time it loops throught plus 1, the third number is to skip every 100.
        num=+ i
        file.write(str(num) + "\n") 
        total+=num
    file.write(str(total) + '\n')
    file.close()

def read():
    file = open("sumOfNumbers.txt", 'r')
    contents = file.readline()
    while contents != '': #theres no space in the  " quotations 
        sumofNums=int(float(contents)) # to get int first float and than int #example int(float(input))
        print(sumofNums)
        contents = file.readline()
    file.close() #dont close the read function
#being gui app
win = tk.Tk() #create the window 
win.geometry("200x75") #w * h in pixels
win.title("Sum The Numbers") #label for the title

sumofNumbers = tk.Label(win,text = "Sum of the Numbers").grid(column = 0, row = 0)

btnRead = tk.Button(win, text= "submit", command=read).grid(column = 0, row =3)
btnWrite = tk.Button(win, text= "write", command=write).grid(column = 1, row =3)
win.mainloop()
win()