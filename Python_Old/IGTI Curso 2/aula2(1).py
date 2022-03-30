# os índices no Python vão de 0 a n-1
# onde n é o tamanho da dimensão
import numpy as np
x = np.linspace(start=10, stop=100, num=10)
print('x:', x)
print('shape:', x.shape)

# extração de elementos
print('x:', x)
print('primeiro elemento:', x[0])
print('segundo elemento:', x[1])
print('último elemento:', x[9])
print('último elemento:', x[-1])
print('elemento:', x[5])

# slicing: extração de subarrays:
print('x:', x)
print('dois primeiros elementos:', x[0:2])  # 2 é exclusivo(n vamos acessar o 2, só o 0 e 1)
print('dois primeiros elementos:', x[:2])
print('dois últimos elementos:', x[-2:])
print('dois ultimos elementos:', x[8:])

# slicing em arrays 2D (matrizes)
x = x.reshape(2, 5)  # reshape de x para 2 linhas e 5 colunas
print('x:\n', x)
# extração de elementos
print('primeira linha, segunda coluna:', x[0, 1])
print('segunda linha, penúltima coluna:', x[1, -2])
print('última linha, última coluna:', x[1, 4])
print('última linha, última coluna:', x[-1, -1])

# slicing: extração de subarrays
print('x:\n', x)
print('primeira linha inteira: ', x[0:])
print('primeira linha, segunda a quarta coluna: ', x[0, 1:4])
print('última coluna inteira:\n', x[:, [-1]])

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print('x antes:', x)
y = x[:2]
y[0] = -100  # alteração do valor em y altera o valor do x
print('x depois:', x)

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print('x antes:', x)
y = x[:2].copy()
y[0] = -100  # alteração do valor em y altera o valor do x
print('x depois:', x)
