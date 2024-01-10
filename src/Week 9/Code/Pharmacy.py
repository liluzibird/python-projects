Create Table Warehouse
(Warehouseid int primary key,
Productid int not null,
StorageLocation TEXT,
Constraint Productid_FK foreign Key (Productid)
references Products (Productid))


Select Products.Productid, Description, UnitCost, RetailPrice, UnitsOnHand,
StorageLocation
from Products, Warehouse
where Products.Productid=Warehouse.Productid
order by Productid asc;





Create Table Patients
(Patientid int primary key,
Name text not null,
  DOB date not null,
     Doctorid int not null)

Create Table Doctors
(Patientid int primary key,
Name text not null,
  DOB date not null,
     License int not null)
     
Create Table Prescriptions
(Prescriptionid int primary key,
Patientid int,
Doctorid int,
P_DATE Date,
DrugCode text,
Constraint Patientid_FK
foreign key (Patientid)
references Patients (Patientid))
Constraint Doctorid)_FK
foreign key (Doctorid)
references Doctors (Doctorid))

Select Products.Productid, Description, UnitCost, RetailPrice, UnitsOnHand,
StorageLocation
from Products, Warehouse
where Products.Productid=Warehouse.Productid and Patients.Patientid
=Prescriptions.Patientid