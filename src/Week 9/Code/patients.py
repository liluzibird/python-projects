#step 1 import libraries
import sqlite3
import os

#Step 2 connect db
con= sqlite3.connect("studentdb.db") #get file location
cur = con.cursor() #conect to db
con.commit #writes to hd

#Print the 3 tables

#Patients Table
print(f'Patients Table')
print('*' * 30)
cur.execute(''' Select * from Patients ''')
resultsPatients=cur.fetchall()
for row in resultsPatients:
    print(f'{row[0] :0} {row[1] :5} {row[2] :2} {row[3] :2}')

 #Doctors Table
print(" ")
print(f'Doctors Table')
print('*' * 30)
cur.execute(''' Select * from Doctors''')
resultsDoctors=cur.fetchall()
for row in resultsDoctors:
    print(f'{row[0] :0} {row[1] :5} {row[2] :2} {row[3] :2}')

#Prescriptions Table
print(" ")
print(f'Prescriptions Table')
print('*' * 30)
cur.execute(''' Select * from Prescriptions ''')
resultsPrescriptions=cur.fetchall()
for row in resultsPrescriptions:
    print(f'{row[0] :0} {row[1] :5} {row[2] :2} {row[3] :2} {row[4] :2}')

 #combine the 3 tables

#executes sql statement to join the tables
print('')
print("Combined Tables")
print('*' * 50)
cur.execute(''' Select Patients.PatientID,Patients.Name,Patients.Birthdate,
Doctors.DoctorID,Doctors.Name, Doctors.Birthdate, Doctors.License,
Prescriptions.PrescriptionID, Prescriptions.PrescriptionDate, Prescriptions.PrescriptionDate,Prescriptions.DrugCode
from Patients,Doctors,Prescriptions
where Patients.PatientID = Prescriptions.PatientID and Doctors.DoctorID = Prescriptions.DoctorID ''')

#stores in variable results
resultsAll=cur.fetchall()
 
#for loop to print the rows
for row in resultsAll: #not printing?? I get no errors but hammer appears here.
    print(f'{row[0] :0} {row[1] :5} {row[2] :2} {row[3] :2} {row[4] :2} {row[5] :2}  {row[6] :2}  {row[7] :2}  {row[8] :2}  {row[9] :2}  {row[10] :2} ')

con.close()