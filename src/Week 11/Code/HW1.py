class Pet:
    def __init__(self, name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_animal_tpe(self):
        return self.__animal_type


def main():
    pet_name = input('Enter name of pet: ')
    pet_type = input('Enter animal type of pet: ')
    pet_age = float(input('Enter age of pet: '))

    pet_desc = Pet(pet_name,pet_type,pet_age)

    print('Pet name is: ', pet_desc.get_name())
    print('Pet type is: ', pet_desc.get_animal_tpe())
    print('Pet age is: ', pet_desc.get_age())

main()