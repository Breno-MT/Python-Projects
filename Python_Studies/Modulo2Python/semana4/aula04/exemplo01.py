class Pessoa1():
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

    @staticmethod
    def printar(self, key):
        print(self.__dict__.get(key))


a = Pessoa1(19, 'Breno')

a.printar('nome')

class Pessoa():
    global ano_atual
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar(self):
        print(f"{self.nome} tem: {self.idade} anos!")

    @classmethod
    def criarPeloAnoDeNascimento(cls, nome, ano_nascimento):
        return cls(nome, ano_atual - ano_nascimento)

pessoa = Pessoa('Joao', 21)
pessoa.mostrar()

pessoa_1 = Pessoa.criarPeloAnoDeNascimento('Breno', 2002)
pessoa_1.mostrar()
