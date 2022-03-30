#### Previne um usuario de criar um objeto daquele class
#### obriga um usuario para dar override abstract methods na classe child
# abstract class = uma classe na qual contem one ou mais metodos abstrados
# abstract method = um metodo que tem uma declaração mas não tem implementação

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive the car!")
    
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    
    
    def go(self):
        print("You ride the motorcycle!")

    def stop(self):
        print("This motorcycle is stopped")
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()