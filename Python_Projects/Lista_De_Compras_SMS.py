import sys
from twilio.rest import Client

# Irá criar o menu aonde todas as funções abaixo foram citadas e explicadas como funcionam.
# É literalmente o Main Menu do nosso código.
def main_menu():

    while True:
        print()
        print(""" [*] Lista de Compras

        1. Ver a lista de compras
        2. Adicionar item a lista
        3. Remover um item da lista
        4. Checar se o item está na lista
        5. Quantos items tem na lista de compras
        6. Limpar a lista
        7. Enviar SMS
        8. Sair

        """)
        # Pergunte o que o usuario deseja realizar
        selecao_numero = input("Digite o número: ")

        # Determina a ação dependendo da seleção do usuario
        if selecao_numero == "1":
            display_list()

        elif selecao_numero == "2":
            add_item()

        elif selecao_numero == "3":
            remove_item()

        elif selecao_numero == "4":
            check_item()

        elif selecao_numero == "5":
            items_in_list()

        elif selecao_numero == "6":
            clear_list()

        elif selecao_numero == "7":
            send_sms()

        elif selecao_numero == "8":
            sys.exit()
        
        else:
            print("Digite uma das seleções acima.")

lista_de_compras = []

# Irá mostrar os items na lista de compras
def display_list():
    print()
    print("[+] Lista de Compras")
    for i in lista_de_compras:
        print("[@] "+i)


# Simplesmente adiciona um item á lista de compras
def add_item():
    print()
    item = input("Digite o item que você quer adicionar na lista: ")
    lista_de_compras.append(item)
    print(f"[!] O item {item} foi adicionado a lista!")


# Remove um item da lista de compras
def remove_item():
    print()
    item = input("Digite o item que você quer remover da lista: ")
    lista_de_compras.remove(item)
    print(f"[!] O item {item} foi removido a lista!")


# Ele irá checkar se um item especifico está na lista de compras
# Obs: Tem que digitar como foi escrito na lista de compras, senão ele não irá achar.
def check_item():
    print()
    print("[+] Checagem de item na lista!")
    check = input("Digite o item para conferir se está na lista: ")
    
    if check in lista_de_compras:
        print(f"O item: '{check}', está na lista de compras!")
    else:
        print(f"O item: '{check}', não está na lista de compras!")


# Irá mostrar o número e os items da lista de compras.
def items_in_list():
    print()
    print(f"Existem {len(lista_de_compras)} número(s) de item(s) na lista de compras. Abaixo o(s) item(s)..")
    for i in lista_de_compras:
        print(f"[~>] {i}")


# Ele irá limpar toda a lista de compras atual. Obs: a lista está default para None, ou seja, não existe item na lista.
def clear_list():
    lista_de_compras.clear()
    print("[!!!] A lista de compras está vazia!")


# Está função irá utilizar o twilio para fazer o envio de SMS
# Para mais informações de como funciona, leia o doc em inglês: www.twilio.com/docs/sms
def send_sms():
    # Account SID from twilio.com/console
    account_sid = "AC71bba9a360d7eeef4a1e51f87ccd7a87"
    # Auth Token from twilio.com/console
    auth_token  = "a9a833b6b8ef43ac8e4bcd9019ac5393"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+5548991112268", 
        from_="+17178373219",
        body=f"Aqui está sua lista de compras! {lista_de_compras}") 

    print(f"Código de confirmação SMS: [->] {message.sid}")


# Está chamando a função que irá sempre mostrar as opções para o usuario digitar.
# Até que saia do programa.
main_menu()