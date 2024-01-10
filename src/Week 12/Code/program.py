import patient
import procedure

def createobjects():
    patient0 = patient.Patient('John','Pika','Doe','Nice street 30',
                               'New York','NY','NY10503',
                               '12341234','Yeadsgfd','13241235')

    procedure1 = procedure.Procedure('Laser αμφιβλιστροϊδή','5/5/1990',
                                     'Dr. Μπαμπης Παπαδημητρίου','30.000 δρχ.')
    procedure2 = procedure.Procedure('Αφαιρεση Χολής', '10/9/2000','Dr Μαρία Τσακαλώτου',
                                     '500 ευρώ')
    procedure3 = procedure.Procedure('Βλαστοκυτταρική αναγέννηση', '23/12/2018',
                                     'Dr Frankenstein', '50.000 ευρώ')
    return(patient0,procedure1,procedure2,procedure3)
def main():
     pat,proc1,proc2,proc3 = createobjects()
     print(pat)
     print()
     print(proc1)
     print()
     print(proc2)
     print()
     print(proc3)

main()