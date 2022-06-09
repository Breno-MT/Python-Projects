import random

count = 0

while count < 3:
    
    lista_numbers = str(random.randrange(0,51,1))
    player_choices = str(input("Digite um número e tente adivinhar!: "))


    if player_choices in lista_numbers:
        print("Parabéns! Você ganhou!")
        count += 1
        continue

    elif player_choices not in lista_numbers:
        print("Você errou! Tente novamente")
        count += 1
        continue








    

