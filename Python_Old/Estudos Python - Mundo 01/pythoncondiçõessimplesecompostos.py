n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) /2
print('Sua média é de {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota está boa! PARABÉNS!')
else:
    print('Sua nota está ruim! ESTUDE MAIS!')
