from  patient import *

class InPatient(Patient):
    def __init__(self,fname,mname,lname,adress,city,state,zipcode,phnum,emname,emphnum,days_in):
        super().__init__(fname,mname,lname,adress,city,state,zipcode,phnum,emname,emphnum)
        self.days_in=days_in
    def set_days(self,days):
        self.days_in=days
    def show(self):
        self.display()
        print('Days:',self.days_in)
        print("The total charge for",self.last_name, "is $",self.days_in*50)

def main():
    smith=InPatient('Will','Thomas','Smith','456 South Street','Dallas','Texas',75050,'214-555-1234','Carol Smith','214-555-4567',3)
    smith.show()

main()