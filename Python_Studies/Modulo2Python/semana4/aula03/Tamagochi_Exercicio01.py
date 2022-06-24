import os
import sys

class Tamagochi:
    def __init__(self, nome = 'Lucius', idade = 9):
        self.nome = nome
        self.idade = idade
        self.__fome = 2.5
        self.__saude = 2.5
        self.__contador = 0

    @property
    def matar(self):
        self.__contador +=1

        if self.__contador > 3:
            print("O seu Tamagochi morreu. Fim de Jogo :(")
            sys.exit()


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

        if self.__fome <= 1:
            print(f"""A fome do {self.nome} já está ok! Não precisa alimentar.
                      Fome atual: {self.__fome}""")
        
        elif self.__fome > 1:
            print(f"Você retirou 0.5 de fome do {self.nome} !")
            self.__fome -= 0.5

    @property
    def give_med(self):
        if self.__saude <= 1:
            print(f"""A saúde do {self.nome} já está ok! Não precisa medicar.
                      Saúde atual: {self.__saude}""")
        
        elif self.__saude > 1:
            print(f"Você retirou 0.5 de fome do {self.nome} !")
            self.__saude -= 0.5
    
    @property
    def status(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Fome: {self.__fome}, Saúde: {self.__saude}")

tamagochi = Tamagochi()

while True:

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
    |    [5] Brincar com Tamagochi
    |    [6] Limpar CMD
    |    [0] Sair
    |
    |   Digite sua opção: """))

    if opcao == 1:
        opcao = tamagochi.change_name()
        tamagochi.matar
    
    elif opcao == 2:
        opcao = tamagochi.give_food
    
    elif opcao == 3:
        opcao = tamagochi.give_med

    elif opcao == 4:
        tamagochi.status
        print("Não deixe a Fome ou Saúde chegar a 5! Ele irá morrer :(")
        tamagochi.matar

    elif opcao == 5:
        print("Você brincou com seu Tamagochi e ele ficou feliz! :D")
        tamagochi.matar

    
    elif opcao == 6:
        os.system("cls")

    elif opcao == 0:
        break

    else:
        print("Digite apenas as opções acima.")
