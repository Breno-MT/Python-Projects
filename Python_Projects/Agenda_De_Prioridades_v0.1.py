import socket
import sys
import os
from time import sleep

# Irá pegar o nome do computador e printar no terminal. Obs: está na função main_menu.
computer_name = socket.gethostname()


# Função para rodar o programa até que seja fechado.
def main_menu():
    
    while True:
        
        print()
        sleep(1)
        print(f""" [->] Bem vindo a sua Agenda {computer_name}!

            1. Mostrar anotações
            
            2. Adicionar anotação

           # 3. Retirar anotação (Em uma futura atualização.)

           # 4. Marcar anotação como concluído (Em uma futura atualização.)

            5. Ajuda (RECOMENDADO: Use para ver ajuda sobre o programa)

            6. Limpar Terminal (Deixar o terminal mais limpo)

            7. Sair
            
        """
        )


        selecao_numero = input("Digite um número: ")

        if selecao_numero == "1":
            show_note()

        elif selecao_numero == "2":
            add_note()

        elif selecao_numero == "3":
            remove_note()

        elif selecao_numero == "4":
            status_note()

        elif selecao_numero == "5":
            help()
        
        elif selecao_numero == "6":
            os.system("cls")

        elif selecao_numero == "7":
            sys.exit()

        else:
            print("Algo deu errado, por favor digite apenas um número.")

# Esta VAR será a lista responsavel por segurar as dict.
lista_de_anotacao = []

# Irá mostrar as anotações em forma crescente, do nivel de prioridade ao menor nivel.
def show_note():
    sleep(1)
    print()
    print("-*-*"*7)
    print("[*] Lista de Anotações!")

    # Irá pegar a chave Nivel, e usara seu valor como base do maior pro menor.
    list_sorted = sorted(lista_de_anotacao, key=lambda value:value["Nivel"], reverse=True)

    if list_sorted == []:
        print("[!] Sua lista está vazia.")
        print("-*-*"*7)

    else:
        for i in list_sorted:
            print(f"[@] {i}")

# Irá adicionar as anotações a uma dict, e irá perguntar o seu nivel de prioridade.
def add_note():
    sleep(1)
    print()

    # Colocando um limite de nivel para que o usuario não passe do limite desejado.
    niveis = [1,2,3,4,5]

    # É aqui que o usuario irá digitar suas anotações.
    anotacao = input("Digite sua anotação: ")
    
    # Está None pois o usuario irá passar um valor para que seja adicionado a dict.
    nivel_estrela = None

    # Apenas tratando o programa para não quebrar ao usar a agenda e perder dados.
    while nivel_estrela not in niveis:    
        try:
            nivel_estrela = int(input("Digite o nivel de prioridade: "))
                
        except ValueError as e:
            print()
            print("-*-*"*7)
            print(f"Ocorreu um erro {e} !")
            print("Coloque apenas números de (1 a 5).")
            print("-*-*"*7)

        except UnboundLocalError as f:
            print()
            print("-*-*"*7)
            print(f"Ocorreu um erro {f} !")
            print("Coloque apenas números de (1 a 5).")
            print("-*-*"*7)
        
        except:
            print()
            print("-*-*"*7)
            print("Ocorreu um erro. Tente novamente.")
        
        if nivel_estrela in niveis:
            continue

        elif nivel_estrela not in niveis:
            print()
            print("-*-*"*7)
            print("Números de 1 a 5 apenas.")
            print("-*-*"*7)
        

    # Está será nossa dict padrão, os valores anotacao, nivel_estrela são passado pelo usuario.
    default_anotacao = {'Anotacao': anotacao, 'Nivel': nivel_estrela, 'Concluido': False}

    # Irá adicionar a dict acima para a lista que foi criada em main_menu.
    lista_de_anotacao.append(default_anotacao)

# Irá remover uma anotação especifica, obs: ainda está em desenvolvimento.
def remove_note():
    print("Esta função está desativada.")

# Irá alterar uma anotação especifica, obs: ainda está em desenvolvimento.
def status_note():
    print("Esta função está desativada.")


# Mostra ajuda sobre o programa
def help():
    sleep(1)
    print()
    print("-*-*"*7)
    print()
    print("""
    Este programa utiliza Sistema de Hierarquia para cada anotação,
    Ou seja, a sua única função com este Programa será apenas definir uma ordem de fazeres,
    E passar qual o seu nível de prioridade no momento.

    ------
    !!! CUIDADO !!!
    Este programa não irá salvar suas anotações em algum tipo de arquivo!!!
    Portanto, não feche o programa caso precise ficar consultando suas anotações!!!
    Ele só irá ficar salvo até o fim do programa para que não consuma nenhum tipo de espaço no computador!!!
    !!! CUIDADO !!!
    ------
    Segue a ordem da hierarquia (Do maior pro menor):
    -> 5
    -> 4
    -> 3
    -> 2
    -> 1  
    ------
    Ajuda sobre Concluído:
    [True] Significa 'Concluído'
    [False] Significa 'Não-Concluído'
    Obs: Na v0.1 essas funções não estão funcionando, apenas irá indicar "False".
    
    Caso precise de ajuda com o programa, contate o criador do mesmo.
    Programa feito por Breno.
    """)
    print("-*-*"*7)

# Chamando a função main_menu para sempre ficar rodando até que o usuario chame a função exit().
main_menu()