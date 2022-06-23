class Pessoa():
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    

    # Método especial para retornar nome, idade
    def __str__(self):
        return str(self.__dict__)

a = Pessoa('Breno', 20)

print(a)
