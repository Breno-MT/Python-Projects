class Animal:
    def comer(self):
        print("O animal come ração pedigre.")

class Peixe(Animal):
    def comer(self):
        print("O peixe não come a ração pedigre")

peixe_1 = Peixe()
peixe_1.comer()
print('--'*5)

super(Peixe, peixe_1).comer()
# super(ClasseFilha, ObjetoInstanciado)