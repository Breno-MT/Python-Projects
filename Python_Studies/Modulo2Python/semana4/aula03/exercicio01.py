class Tamagochi:
    def __init__(self, nome, idade, fome, saude):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude
    
    def change_name(self):
        pass

    def give_food(self):
        pass

    def give_med(self):
        pass
    

    # Método especial para retornar nome, idade, fome e saude
    def __str__(self):
        return str(self.__dict__)