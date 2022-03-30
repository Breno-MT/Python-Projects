import random
import sys

# Main menu é o nosso menu que irá sempre aparecer até utilizarmos a opção Nº 3. 
def main_menu():
    
    while True:

        print()
        print(""" [>] Gerador de Senha! [<]
                  Selecione uma das opções abaixo.

            1. Gerar Senha
            2. Info
            3. Sair

        """
        )
        escolha_numero = input("Digite sua opção: ")
        
        if escolha_numero == "1":
            pwd_generator()

        elif escolha_numero == "2":
            show_info()

        elif escolha_numero == "3":
            exit()

        else:
            print("Por favor digite uma das opções válidas.")  

# Letras aleatórias que o pwd_generator irá utilizar para fazer a senha.
letras = "abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&^*-_"


# Irá gerar uma das várias, ou não, senhas escolhidas pelo usuário.
def pwd_generator():

    # Tamanho e quantidade da senha.
    password_tamanho = int(input("Qual o tamanho da sua senha?: "))
    password_quantidade = int(input("Quantas senhas você deseja ter?: "))


    print(f"Aqui está sua(s) senha(s)!")

    # Irá pegar a password que está nula, e irá montar ela baseada no password_tamanho e password_quantidade.
    for i in range(0, password_quantidade):
        password = ""
        for h in range(0, password_tamanho):
            password_letras = random.choice(letras)
            password = password + password_letras
        print(f"[*] {password}")

# Irá mostrar informações sobre quando o programa foi criado e por quem.
def show_info():
    print("[-] Info sobre o programa")
    print("-*-"*5)
    print("Este projeto teve ínicio no dia 18/01/2022, feito por Breno.")

# Simplesmente irá fechar o programa.
def exit():
    sys.exit()


# Tem que deixar o main_menu() de fundo, pois é ele quem chama a função que encarrega das outras funções, e obviamente, irá nos mostrar o menu.
main_menu()