from patient import *

def main():
    jones=Patient('James','Edward','Jones','123 Main Street','Billings','Montana',59000,'406-555-1212','Jenny Jones','406-555-1213')
    physicalexam=Procedure('Physical Exam','8-24-2019','Dr.Irvine',250.00)
    xray=Procedure('X-ray','8-24-2019','Dr.jamison',500.00)
    bloodtest=Procedure('Blood test','8-24-2019','Dr.Smith',200.00)
    jones.set_procedure_list([physicalexam,xray])
    jones.display()
    list_of_poce=[physicalexam,xray,bloodtest]
    for procedure in list_of_poce:
        print()
        procedure.display()
    print('\nProcedures performed on the patients are')
    for procedure in jones.get_procedure_list():
        print()
        procedure.display()
    jones.caluclate_charges()

main()