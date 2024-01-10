class Employee:
	def GetInformation(self):
		print("Employee name is " + self.Name)
		print("Employee ID number is " + self.IDNumber)
		print("Employee department is " + self.Department)
		print("Employee job title is " + self.JobTitle)

Employee1 = Employee()
Employee1.Name = "Susan Meyers"
Employee1.IDNumber = "47899"
Employee1.Department = "Accounting"
Employee1.JobTitle = "Vice President"

Employee2 = Employee()
Employee2.Name = "Mark Jones"
Employee2.IDNumber = "39119"
Employee2.Department = "IT"
Employee2.JobTitle = "Programmer"

Employee3 = Employee()
Employee3.Name = "Joy Rogers"
Employee3.IDNumber = "81774"
Employee3.Department = "Manufacturing"
Employee3.JobTitle = "Engineer"



Employee1.GetInformation()

Employee2.GetInformation()

Employee3.GetInformation()