string_inteiros = input('Entre com uma lsita de inteiros: ')
lista_inteiros = string_inteiros.split()
contador = 0
for inteiro in lista_inteiros:
    contador = contador + 1
print('Existem %.d inteiros na lista' % contador)
