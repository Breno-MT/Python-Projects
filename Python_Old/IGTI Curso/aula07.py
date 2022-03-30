#definindo a função em Python
def equação_reta(x):
    y_x = 2 * x + 1
    return y_x
#chamando a função
x = float(input('Entre com um valor a ser calculado para y(x)=2x + 1 : '))
resultado = equação_reta(x)
print('O resultado encontrado é y=%2.d' % resultado)

#imagine calcular os valores de y para uma lista de valores

lista_x = [1, 2, 3, 2.5, 10, 45, 88, 123.4]
#y_1 = 2 * lista_x[0] +1
#y_2 = 2 * lista_x[1] +1
#y_3 = 2 * lista_x[2] +1
#y_4 = 2 * lista_x[3] +1
#y_5 = 2 * lista_x[4] +1
#y_6 = 2 * lista_x[5] +1
#y_7 = 2 * lista_x[6] +1
#y_8 = 2 * lista_x[7] +1

#utilizando funções
lista_y = []
for valor_x in lista_x:
    lista_y.append(equação_reta(valor_x))
print(lista_y)
