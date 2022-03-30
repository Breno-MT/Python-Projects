### Duck Typing = conceito aonde a classe de um objeto é menos importante do que methods/attributes
# tipo de classe não é checkada se o minimo de methods/attributes estão presentes
# "Se anda como um pato, e faz quack como um pato, então deve ser um pato"

class Duck:

    def walk(self):
        print("This duck is walking!")
    
    def talk(self):
        print("This duck is qwuacking!")

class Chicken:
    def walk(self):
        print("This chicken is walking!")
    
    def talk(self):
        print("This chicken is clucking!")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)