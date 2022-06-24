import random

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"{self.nome} tem: {self.idade} anos!")

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

lista_nomes = ['Breno', 'Maycon', 'Kauan', 'Yan']

# lista_random = random.choices(lista_nomes)
lista_random = random.shuffle(lista_nomes)

lista_idade = [random.randint(20, 40)]

lista_alunos = []

for _ in range(1,31):
    x = Aluno(lista_random, lista_idade)
    lista_alunos.append(x)
    x.isApproved()

print(*lista_alunos, sep = "\n")

