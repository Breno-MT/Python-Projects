class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criarPeloAnoNascimento(cls, nome, nascimento):
        return cls(nome, 2022 - nascimento)
    
    def mostrar(self):
        print(f"{self.nome} tem: {self.idade} anos!")

class Aluno(Pessoa):
    def __init__(self, nome, idade):
        self.nome = nome
        self.nota = 0
        self.idade = idade
    
    def darNota(self, nota):
        self.nota = nota
        print(f"{self.nome} recebeu nota {self.nota}")
    
    @staticmethod
    def periodoLetivo():
        print("O período letivo para o semestre X vai do dia tal até tal")

pessoa_1 = Aluno.criarPeloAnoNascimento('Breno', 2002)
pessoa_1.mostrar()
pessoa_1.darNota(10)
