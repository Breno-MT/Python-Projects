import random

nomes = ["Breno", "Eric", "Maycon", "Yan", "Joao", "Kauan", "Farias", "Gabriel"]

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Nota: {self.nota}")

    @classmethod
    def criarPeloAno(cls, nome, ano_nascimento):
        return cls(nome, 2022 - ano_nascimento)
    
    def __str__(self):
        return str(self.__dict__)

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso = "DevInHouse"):
        self.nome = nome
        self.idade = idade
        self.nota = random.randint(1,10)
        self.curso = curso
    
    def darNota(self, nota):
        self.nota = nota
        print(f"{self.nome} recebeu nota {self.nota}")
    
    def isApproved(self):
        if self.nota >= 7:
            print(f"{self.nome} está aprovado! Nota: {self.nota}")
        
        elif self.nota < 7:
            print(f"{self.nome} está reprovado, estude mais! Nota: {self.nota}")

# nomes[random.randint(0, len(nomes) -1)]

for i in range(30):
    aluno = Aluno(nomes[random.randint(0, len(nomes) -1)], random.randint(18, 50))
    aluno.darNota(random.randint(1,10))
    aluno.mostrar()
    aluno.isApproved()
