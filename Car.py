class Car:
    wheels = 4

    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.parking = 0


    def drive(self, distance):
        self.odometer += distance
        return f"Driving {distance} km. Total: {self.odometer} km"

    def parking (self, hour):
        self.parking = self.parking + hour
        return f"Total parking = {self.parking}"

my_car1 = Car("Toyota", "Corolla", 2020)
print(my_car1.make)  # Вывод: Toyota
print(my_car1.drive(100))  # Вывод: Driving 100 km. Total: 100 km

my_car2 = Car("Captiva", "Dewoo", 2025)
print(my_car2.drive(60))  # Вывод: Driving 100 km. Total: 100 km
#print(my_car2.parking(120))

