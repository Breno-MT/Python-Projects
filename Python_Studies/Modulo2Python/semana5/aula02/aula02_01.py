class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando!')

class Medico(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def atender(self):
        print(f"Médico {self.nome} está atendendo...")


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def comprar(self):
        print(f"Cliente {self.nome} está comprando...")


class Aluno(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def estudar(self):
        print(f"Aluno {self.nome} está estudando...")

Medico('Breno', 20).atender()
Cliente('Natan', 22).comprar()
Aluno('Maycon', 22).estudar()
