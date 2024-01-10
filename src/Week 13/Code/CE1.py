class AnimalType:
	def eats(self):
		print("This animal likes to eat?")

class rabbits(AnimalType):
	def munch(self):
		print(" carrots ")

class birds(rabbits):
	def munch1(self):
		print(" seeds ")


class dogs(AnimalType):
	def munch2(self):
		print(" dog food ")

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()


BirdObject = birds()
BirdObject.eats()
BirdObject.munch1()

DogObject = dogs()
DogObject.eats()
DogObject.munch2()