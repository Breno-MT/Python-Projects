from random import sample, seed

# seed(1)

tamanho = 6

lista_numero = []

resultado_random = sample(range(1,61), tamanho)
print(f"Resultado {resultado_random}")

def check_numbers():

    acertos = len(set(lista_numero) & set(resultado_random))
    print("---"*10)
    print(f"Estes foram seus números! -> {lista_numero}")
    print(f"Estes foram os número da Mega Sena! -> {resultado_random}")
    print(f"Você acertou! {acertos}")
    
while True:

    print("Digite no máximo 6 números 1 de cada vez")
    numero_escolhas = int(input("Digite os números:"))
    lista_numero.append(numero_escolhas)
    
    if len(lista_numero) >= 6:
        check_numbers()
        break
