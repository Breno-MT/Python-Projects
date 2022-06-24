import os

class Tamagochi:
    def __init__(self, nome = 'Lucius', idade = 9):
        self.nome = nome
        self.idade = idade
        self.__fome = 2.5
        self.__saude = 2.5

    def change_name(self):
        opcao = str(input(f"""Você gostaria de mudar o nome do seu Tamagochi? 
            Nome atual: {tamagochi.nome}
            S/N -> """))

        opcao.lower()

        if opcao == 's':
            nome_alterado = str(input("Digite o nome que deseja: "))
            self.nome = nome_alterado
        
        elif opcao == 'n':
            print('Você cancelou essa operação.')
        
    @property
    def give_food(self):

        if self.__fome < 1:
            print(f"""A fome do {self.nome} já está ok! Não precisa retirar.
                      Fome atual: {self.__fome}""")
        
        elif self.__fome > 1:
            print(f"Você retirou 0.5 de fome do {self.nome} !")
            self.__fome -= 0.5

    @property
    def give_med(self):
        if self.__saude < 1:
            print(f"""A saúde do {self.__saude} já está ok! Não precisa retirar.
                      Saúde atual: {self.__fome}""")
        
        elif self.__saude > 1:
            print(f"Você retirou 0.5 de fome do {self.nome} !")
            self.__saude -= 0.5
    

    # Método especial para retornar nome, idade, fome e saude
    def __str__(self):
        return str(self.__dict__)

tamagochi = Tamagochi()

while True:

    count = 0

    opcao = int(input(f""" Bem-vindo ao seu Tamagochi!
    ______________________________________________________
    |                               ****/            
    |                           .**, &/& ,//.        
    |                         *//  @   @  ///       
    |                       **/////////////////     
    |                       *////////////////////    
    |                     *//////_________/////////   
    |                     */////|        ////////   
    |                     //////|_______//////(    
    |                         ##//////(((%# 
    |
    |
    |    [1] Mudar nome
    |    [2] Dar Comida
    |    [3] Dar Remédio
    |    [4] Imprimir status
    |    [5] Limpar CMD
    |    [0] Sair
    |
    |   Digite sua opção: """))


    if opcao == 1:
        opcao = tamagochi.change_name()
        count += 1
    
    elif opcao == 2:
        opcao = tamagochi.give_food
    
    elif opcao == 3:
        opcao = tamagochi.give_med

    elif opcao == 4:
        print(tamagochi)
        print("Não deixe a Fome ou Saúde chegar a 5! Ele irá morrer :(")
        count += 1

    elif opcao == 5:
        os.system("cls")

    elif opcao == 0:
        break

    else:
        print("Digite apenas as opções acima.")