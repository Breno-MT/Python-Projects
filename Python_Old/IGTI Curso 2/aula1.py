#Criação de Array
import numpy as np

#array 1D = [1, 2, 3]
#x = np.array([1, 2, 3]) é uma possibilidade também
l = [1, 2, 3]
x = np.array(l )#, dtype=int) para forçar apenas nm int.
print('x:', x)
print('shape:', x.shape)
print(type(x))

#criação de um array 2D: listas aninhadas
l = [[1, 2], [3, 4]]
x = np.array(l)
print('x:\n', x)
print('shape:', x.shape)

#array contendo apenas 0's(zeros)
dim = (2, 2) #(3, 3) para ter 3 linhas e 3 colunas e assim vai  # (linhas, colunas)
x = np.zeros(dim)
print('x:\n', x)
print('shape:', x.shape)

#array contendo apenas 1's(um)
size = (2, 2)  # (linhas, colunas)
x = np.ones(size)
print('x:\n', x)
print('shape:', x.shape)

#criação de valores dentro de um intervalo
# valores uniformes entre 5 e 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6)
print('x:', x)
print('shape:', x.shape)

# criação da matriz identidade
n = 4
x = np.eye(n)
print('x:\n', x)
print('shape:', x.shape)

#criação de valores aleatórios
# np.random.seed(10)
x = np.random.random(size=(2, 3))
print('x:\n', x)
print('shape:', x.shape)