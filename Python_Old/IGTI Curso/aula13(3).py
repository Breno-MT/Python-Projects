class Carro:
    def __init__(self, numero_portas, preço):
        self.numero_portas = numero_portas
        self.preço = preço
    print('Objeto carro instancionado com sucesso.')
    def get_numero_portas(self):
        return self.numero_portas
    def set_numero_portas(self, novo_numero_portas):
        self.numero_portas = novo_numero_portas

carro_3 = Carro(4, 50000)
print('Número de portas antes: ', carro_3.get_numero_portas())  #método get, não modifica o estado do objeto
carro_3.set_numero_portas(2)  #modifica o estado do objeto
print('Novo número de portas: ', carro_3.get_numero_portas())

#cria a referencia ao objeto carro
carro_4 = carro_3
print('Número de portas carro_4: ', carro_4.get_numero_portas())

#modificando o número de portas do carro_4
carro_4.set_numero_portas(3)
print('Novo número de portas do carro_4: ', carro_4.get_numero_portas())

#numero de portas do carro_3
print('Número de portas do carro_3: ', carro_3.get_numero_portas())