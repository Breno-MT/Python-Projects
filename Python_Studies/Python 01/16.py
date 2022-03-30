############################# Python Object Oriented Programming ( POOP )
############################# in Python, don't need to pass information to "self", it does already
from car import Car

#car_1 = Car("Chevy","Corvette",2021,"blue")
#car_2 = Car("Ford","Mustang",2022,"red")

#car_1.drive()
#car_2.stop()

############################# class variables

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
