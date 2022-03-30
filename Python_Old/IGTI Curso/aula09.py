def verifica_divisibilidade(x, y):
    return int(y) % int(x) == 0
    
def elementos_divisiveis(x, lista):
    resultado = []

    for elemento in lista:
        if verifica_divisibilidade(elemento, x):
            resultado.append(elemento)
    return resultado

def divisores_em_lista(lista):
    for elemento in lista:
        print(elemento, ' é divisível por ', end=' ')
        elementos = elementos_divisiveis(elemento, lista)
        for f in elementos:
            print(f, end=' ')
        print()

s = input('Entre com uma sequência de valores separados por espaço: ')
lista_valores = []
for x in s.split():
    lista_valores.append(int(x))
divisores_em_lista(lista_valores)
