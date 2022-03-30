import random
while True:
    choices = ["pedra", "papel", "tesoura"]

    computador = random.choice(choices)
    jogador = None

    while jogador not in choices:
        jogador = input("pedra, papel or tesoura?: ").lower()
        if jogador == computador:
            print("computador: ", computador)
            print("jogador: ", jogador)
            print("It's a tie!")
        elif jogador == "pedra":
            if computador == "papel":
                print("computador: ", computador)
                print("jogador: ", jogador)
                print("Você perdeu!")
            if computador == "tesoura":
                print("computador: ", computador)
                print("jogador: ", jogador)
                print("Você ganhou!")
        elif jogador == "tesoura":
            if computador == "pedra":
                print("computador: ", computador)
                print("jogador: ", jogador)
                print("Você perdeu!")
            if computador == "papel":
                print("computador: ", computador)
                print("jogador: ", jogador)
                print("Você ganhou!")
        elif jogador == "papel":
            if computador == "tesoura":
                print("computador: ", computador)
                print("jogador: ", jogador)
                print("Você perdeu!")
            if computador == "pedra":
                print("computador: ", computador)
                print("jogador: ", jogador)
                print("Você ganhou!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye! Have a good day!")    