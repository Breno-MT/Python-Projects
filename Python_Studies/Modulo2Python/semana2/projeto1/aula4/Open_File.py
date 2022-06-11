f = open('texto.txt', 'r')
print(f.read())


with open('texto.txt', 'r'):
    lista = f.read().splitlines()

print(lista)