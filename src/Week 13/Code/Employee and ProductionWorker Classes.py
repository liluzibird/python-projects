class Employee:
	def __init__(self, name, number):
		self.__name = name
		self.__employee_num = number

	def set_name(self, name):
		self.__name = name

	def set_employee_number(self, number):
		self.__employee_num = number

	def get_name(self):
		return self.__name

	def get_employee_number(self):
		return self.__employee_num

class ProductionWorker(Employee):
	def __init__(self, name, number, shift_num, hourly_pay):
		if shift_num == 1 or shift_num == 2:
			self.__shift = shift_num
		else:
			raise ValueError('The shift number should either be 1 or 2.')
		self.__hourly_pay = float(hourly_pay)
		Employee.__init__(self, name, number)

	def set_shift_number(self, shift_num):
		if shift_num == 1 or shift_num == 2:
			self._shift = shift_num
		else:
			raise ValueError('The shift number should either be 1 or 2.')

	def set_hourly_pay(self, hourly_pay):
		self.__hourly_pay = float(hourly_pay)

	def get_shift(self):
		if self.__shift == 1:
			return 'day'
		else:
			return 'night'

	def get_hourly_pay(self):
		return format(self.__hourly_pay, ',.2f')

def main():
	john = ProductionWorker('John Doe', 1234, 1, 12.34)

	print('Name: ', john.get_name())
	print('Employee Number: ', john.get_employee_number())
	print('Shift: ', john.get_shift().title())
	print('Hourly Pay: $', john.get_hourly_pay())
	
main()