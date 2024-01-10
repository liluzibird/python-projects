class person:

    def __init__(self, name, age, address,city,state,zipcode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Student(person):
    def __init__(self,name,age,address,city,state,zipcode,StudentID,GPA):
        super().__init__(name,age,address,city,state,zipcode)#call the super class (person) for the name, and age
        #parameters

        Name = input("Enter the name of the student ")
        Age = int(input("Enter the age of the student "))
        ADDRESS = input ("Enter the address of the student ")
        CITY = input ("Enter the city of the student ")
        STATE = input ("Enter the state of the student ")
        ZIP = int(input ("Enter the zipcode of the student "))



        self.SID = StudentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, address,city,state,zipcode, TeacherID,ClassTeaching):
      super().__init__(name,age,address,city,state,zipcode,TeacherID,ClassTeaching)

    
      Name = input("Enter the name of the teacher ")
      Age = int(input("Enter the age of the teacher "))
      ADDRESS = input ("Enter the address of the teacher ")
      CITY = input ("Enter the city of the teacher ")
      STATE = input ("Enter the state of the teacher ")
      ZIP = int(input ("Enter the zipcode of the teacher "))
      TID = input ("Enter the TID of the teacher ")
      CT = input("Enter the course teaching ")
      #room = input ("Enter the room # of the teacher ")
      self.TID =TeacherID
      self.CT = ClassTeaching
      #self.room = Room
      

student = Student ("Jane Doe",25,"111 St","Santa Ana","CA",12345, 777,3.8)
print("Student Name: " , student.name)
print("Student Age: " , student.age)
print("Student Address: " , student.address)
print("Student City: " , student.city)
print("Student State: " , student.state)
print("Student Zipcode: " , student.zipcode)
print("Student ID: " , student.SID)
print("Student GPA: " , student.GPA)

print("\n")
teacher = Teacher("Ms. Cantor ", 45, "222 St", "Garden Grove","CA",78976, 7, "Python Programming")
print("Teacher Name: " , teacher.name)
print("Teacher Age: " , teacher.age)
print("Teacher Address: " , teacher.address)
print("Teacher City: " , teacher.city)
print("Teacher State: " , teacher.state)
print("Teacher Zipcode: " , teacher.zipcode)
print("Teacher ID: " , teacher.TeacherID)
print("Teacher Course: " , teacher.ClassTeaching)
#print("Teacher Room#: " , teacher.room)




