#criando uma classe Carro
class Carro:
    def __init__(self,numero_portas,preço):
        self.numero_portas=numero_portas
        self.preço=preço
        print('Objeto carro instanciado com sucesso.')
    def get_numero_portas(self):
        return self.numero_portas
    def get_preço(self):
        return self.preço

carro_1 = Carro(4, 50000)
portas_carro_1 = carro_1.get_numero_portas()
print('Meu carro possui %d portas.' % portas_carro_1)
preço_do_carro = carro_1.get_preço()
print('O valor do carro é %d R$!' % preço_do_carro)

#carro 2
carro_2 = Carro(2, 80000)
portas_carro_2 = carro_2.get_numero_portas()
print('Meu carro possui %d portas.' % portas_carro_2)
preço_do_carro_2 = carro_2.get_preço()
print('O valor do carro 2 é %d R$!' % preço_do_carro_2)
