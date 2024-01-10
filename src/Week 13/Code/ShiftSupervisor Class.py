class Shiftsupervisor:
    def __init__(self, salary, bonus):
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus

class Employee:
    def __init__(self, salary, bonus, name, idnum):
        self.salary = salary
        self.bonus = bonus
        self.name = name
        self.idnum = idnum

class ShiftSupervisor(Employee):
    def __init__(self, salary, bonus, name, idnum, shift_number):
        super().__init__(salary, bonus, name, idnum)
        self.shift_number = shift_number

def main():
    shift1 = ShiftSupervisor(30000.0, 1000.00, 'John Doe', 'S10001', 1)
    shift2 = ShiftSupervisor(30000.0, 1000.00, 'Jane Doe', 'S20202', 2)

    find_income(shift1)
    find_income(shift2)

def find_income(employee):
    production = input('Did shift {0} make quota this year? Type Y for yes '.format(employee.shift_number))
    if production.lower() == 'y':
        total_income = employee.salary + employee.bonus
    else:
        total_income = employee.salary
    print("{0}'s Total income is: ${1}".format(employee.name, total_income))
def total_income():
    if production == 'y' or 'Y':
        return __salary + __bonus
    else:
        return __salary

    production = input('Did Shift 1 make quota this year? Type Y for yes ' )

    print(shift1.get_name(),'s Total income is: $', format(total_income, \
        ',.2f'), sep='')


    production = input('Did Shift 2 make quota this year? Type Y for yes ' )

    print(shift2.get_name(),'s Total income is: $', format(total_income, \
        ',.2f'), sep='')


main()