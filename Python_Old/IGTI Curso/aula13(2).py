#Métodos acessores e modificadores
# GETTERS (Métodos Acessores)
#Setters (Métodos Modificadores)

#importando o modulo array
import array as ar

#inicializando o array
meu_array = ar.array('i', [5, 1, 3, 4, 2, 2, 7])

#print do array
print(meu_array)

#acessando o indice do valor igual a 2
print(meu_array.index(2))

#acessando a quantidade de valores 2 existentes
print(meu_array.count(2))

#classes que nao possuem métodos mutáveis - int, float, string
string = 'Estou estudando Python'
print(id(string))
string = string + ' no IGTI.'
print(id(string))
print(string)