############################# method overriding

class Animal:
    def eat(self):
        print("This animal is eating!")

class Rabbit(Animal):
    def eat(self):
        print("This Rabbit is eating a carrot!") # ignorou oq o de cima falou, method overriding.

rabbit = Rabbit()
rabbit.eat()
