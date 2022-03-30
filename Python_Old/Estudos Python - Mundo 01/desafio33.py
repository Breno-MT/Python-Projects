a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
### Menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor foi {}!' .format(menor))
# Maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor foi {}!' .format(maior))
