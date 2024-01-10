import vehicles

def main():
	used_car = vehicles.Automobiles("Audi", 2022, 4500, 80000.0, 2)
	print("Make: ", used_car.get_make())
	print("Model: ", used_car.get_model())
	print("Mileage: ", used_car.get_mileage())
	print("Price: ", used_car.get_price())
	print("Doors: ", used_car.get_doors())

	used_car = vehicles.Automobiles("Honda", 2022, 4500, 80000.0, 4)
	print("\nMake: ", used_car.get_make())
	print("Model: ", used_car.get_model())
	print("Mileage: ", used_car.get_mileage())
	print("Price: ", used_car.get_price())
	print("Doors: ", used_car.get_doors())

	used_car = vehicles.Automobiles("Smart", 2022, 4500, 80000.0, 4)
	print("\nMake: ", used_car.get_make())
	print("Model: ", used_car.get_model())
	print("Mileage: ", used_car.get_mileage())
	print("Price: ", used_car.get_price())
	print("Doors: ", used_car.get_doors())
	
main()