from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class SUV(Car):
    def drive(self):
        print("Driving SUV")

class Sedan(Car):
    def drive(self):
        print("Driving Sedan")

class CarFactory:
    def create_car(self, car_type):
        if car_type == "SUV":
            return SUV()
        elif car_type == "Sedan":
            return Sedan()
        else:
            return None

# Example usage:
factory = CarFactory()
suv = factory.create_car("SUV")
sedan = factory.create_car("Sedan")

suv.drive() # Output: Driving SUV
sedan.drive() # Output: Driving Sedan