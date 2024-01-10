import datetime
class Patient:
    def __init__(self,fname,mname,lname,adress,city,state,zipcode,phnum,emname,emphnum):
        self.first_name=fname
        self.middle_name=mname
        self.last_name=lname
        self.adress=adress
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.phone_number=phnum
        self.emergency_name=emname
        self.emergency_phone_number=emphnum
        self.procedure_list=[]
    def get_first_name(self):
        return self.first_name
    def get_middle_name(self):
        return self.middle_name
    def get_last_name(self):
        return self.last_name
    def get_adress(self):
        return self.adress
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_zipcode(self):
        return self.zipcode
    def get_phone_number(self):
        return self.phone_number
    def get_emergency_name(self):
        return self.emargency_name
    def get_emergency_phone_number(self):
        return self.emergency_phone_number
    def get_procedure_list(self):
        return self.procedure_list
    def set_first_name(self,first_name):
        self.first_name=first_name
    def set_middle_name(self,middle_name):
        self.middle_name=middle_name
    def set_last_name(self,last_name):
        self.last_name=last_name
    def set_adress(self,adress):
        self.adress=adress
    def set_city(self,city):
        self.city
    def set_state(self,state):
        self.state=state
    def set_zipcode(self,zipcode):
        self.zipcode=zipcode
    def set_phone_number(self,phone_number):
        self.phone_number=phone_number
    def set_emergency_name(self,emargency_name):
        self.emargency_name=emargency_name
    def set_emergency_phone_number(self,emergency_phone_number):
        self.emergency_phone_number=emergency_phone_number
    def set_procedure_list(self,procedure_list):
        self.procedure_list=procedure_list
    def caluclate_charges(self):
        total_charges=0
        for procedure in self.procedure_list:
            total_charges=total_charges+procedure.get_charges()
        print('\nThe total charges for ',self.last_name,'is',total_charges)
    def display(self):
        print('First Name:',self.first_name)
        print('Middle Name:',self.middle_name)
        print('Last name:',self.last_name)
        print('Address:',self.adress)
        print('City:',self.city)
        print('State:',self.state)
        print('ZIP:',self.zipcode)
        print('Phone:',self.phone_number)
        print('Emergency Contact:',self.emergency_name)
        print('Emergency Phone:',self.emergency_phone_number)




class Procedure:
    def __init__(self,procedure_name,date,practitioner_name,charges):
        self.procedure_name=procedure_name
        self.date=date
        self.practitioner_name=practitioner_name
        self.charges=charges
    def get_procedure_name(self):
        return self.procedure_name
    def get_date(self):
        return self.date
    def get_practitioner_name(self):
        return self.practitioner_name
    def get_charges(self):
        return self.charges
    def set_procedure_name(self,procedure_name):
        self.procedure_name=procedure_name
    def set_date(self,date):
        self.date=date
    def set_practitioner_name(self,practitioner_name):
        self.practitioner_name=practitioner_name
    def set_charges(self,charges):
        self.charges=charges
    def display(self):
        print('Procedure:',self.procedure_name)
        print('Date',self.date)
        print('Practitioner:',self.practitioner_name)
        print('Charge',self.charges)