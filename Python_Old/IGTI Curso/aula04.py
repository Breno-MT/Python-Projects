for i in range(1,10,2):
    print(i1)
print('--- FIM ---')

for i in range(10,0,-2):
    print(i)
print('...')
################################
string = input('Entre com alguma string: ')
for caracter in range(len(string)-1,-1,-1):
    print(string[caracter])
print('--- FIM ---')
################################
string = 'Eu estou estudando python blabla'
for palavras in string.split():
    print(palavras)
print('--- FIM ---')
