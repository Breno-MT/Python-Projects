# Fazer uma interface
import random
import sys
from time import sleep

# Fazer um programa que pergunte ao jogador para rolar o dice; logo após, mostrar o número e perguntar se ele quer rolar novamente.

while True: # Enquanto o programa não receber False, ele irá continuar.

    dice_numbers = [1,2,3,4,5,6]
    dice = random.choice(dice_numbers)

    player_digit = str(input('Wanna roll the dice? (y/n): '))
    player_digit.lower()
    
    if player_digit != 'y':
        print('See you soon! :(')
        break
    while player_digit == 'y':
        print('---- LET THE GAME BEGIN! ----')
        sleep(0.85)
        print('Rolling Dice in...')
        print('*-*-'*2)
        sleep(1)
        print('1!')
        print('*-*-'*2)
        sleep(1)
        print('2!!')
        print('*-*-'*2)
        sleep(1)
        print('3!!!')
        print('*-*-'*2)
        print(f"Dice's number is: {dice}!")
        print('*-*-'*2)
        sleep(1)
        
        # Caso de 2, vai mostrar isso kkkk, só uma brincadeira mesmo.
        if dice == 2:
            print('Secret Message!!! :O')
            print('*-*-'*2)
   
        
        jogar_novamente = str(input('Wanna roll the dice again? (y/n): '))
        jogar_novamente.lower()
        if jogar_novamente != 'y':
            sys.exit()
