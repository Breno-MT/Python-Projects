class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def comer(self):
        print("Este animal está comendo!")

class Felino:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def comer(self):
        print("Este felino está comendo!")

class Gato(Animal, Felino):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        super().comer()

gato = Gato("Dmitri", "siames")

print(f"O nome desse gato é {gato.nome}, sua cor é {gato.cor} !")
# gato.comer()
