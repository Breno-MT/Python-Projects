class Pessoa:
    def __init__(self, pessoa, valor_retornado = 0):
        self.pessoa = pessoa
        self.valor_retornado = valor_retornado
    
    def calcularComissao(self, vendas = 1000):
        self.valor_retornado = vendas * 0.1
    
class VendedorPJ(Pessoa):
    def __init__(self, pessoa, valor_retornado = 0):
        super().__init__(pessoa, valor_retornado)

class VendedorCLT(Pessoa):
    def __init__(self, pessoa, valor_retornado=0):
        super().__init__(pessoa, valor_retornado)

    def calcularComissao(self, vendas=1000):
        self.valor_retornado = vendas * 0.03 + 1100