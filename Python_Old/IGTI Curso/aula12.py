import sys
print(sys.path)
import math

print('O valor de pi é: ', math.pi)
print('O seno de 45graus é: ', math.sin(math.pi / 4))
print('O cosseno de 180graus é: ', math.cos(math.pi))

import math, datetime
print(datetime.datetime.now())

print('Módulo string: ', str(124))
print('Módulo float: ', float(123 / 12))

import platform
x = platform
plataforma = x.system()
print(plataforma)
print(x.python_version())
print(x.processor())
