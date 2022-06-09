import random

count = 1

while count < 4:
    
    lista_numbers = random.randint(0,51)
    player_choices = int(input("Digite um número e tente adivinhar!: "))


    if player_choices == lista_numbers:
        print("-*-"*6)
        print("Parabéns! Você ganhou!")
        print(f"Tentativas restantes: {count}")
        print("-*-"*6)
        count += 1
        continue

    elif player_choices != lista_numbers:
        print("-*-"*6)
        print("Você errou! Tente novamente")
        print(f"Tentativas restantes: {count}")
        print("-*-"*6)
        count += 1
        continue








    

