class Person:
  def __init__(self, name, address, telephone) -> None:
    self.name = name
    self.address = address
    self.telephone = telephone

class Customer(Person):
  def __init__(self, name, address, telephone, customer_number, mailing_list) -> None:
    super().__init__(name, address, telephone)

    self.customer_number = customer_number
    self.mailing_list = mailing_list

  def get_name(self):
    return self.name

  def get_address(self):
    return self.address

  def get_telephone(self):
    return self.telephone

  def get_customer_number(self):
    return self.customer_number

  def get_mailing_list(self):
    return self.mailing_list

length = int(input('How many records do you want to create? '))

customers = []

for i in range(length):
  print()
  print('Record number:', (i + 1))
  print()

  name = input('Enter name: ')

  address = input('Enter address: ')

  telephone = input('Enter telephone: ')

  customer_number = input('Enter customer number: ')

  join_mailing = input('Join mailing list? (y/n): ') == 'y'

  customer = Customer(name, address, telephone, customer_number, join_mailing)

  customers.append(customer)

print(f'Name\t\tAddress\t\t\tTelephone\t\tCustomer number\t\t\tMailing list joined')

for customer in customers:
  print(f'{customer.get_name()}\t\t{customer.get_address()}\t\t{customer.get_telephone()}\t\t\t{customer.get_customer_number()}\t\t\t\t{customer.get_mailing_list()}')