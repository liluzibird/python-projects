
class Car(object):

    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        #Accelerate car.
        self.__speed += 5

    def brake(self):
        #Decelerate car.
        self.__speed -= 5

    def get_speed(self):
        #Get current speed of car.
        return self.__speed


def main():
    # create a Car object
    car = Car("2001", "Toyota Camry")
    # calls the accelerate method
    print ("2001 Toyota Camry Accelerating . . .")

    for i in range(5):
        car.accelerate()
        print (car.get_speed())


    # calls the brake method five times.
    print ("2001 Toyota Camry Decelerating . . .")

    for i in range(5):
        car.brake()
        print (car.get_speed())

if __name__ == "__main__":
    main()