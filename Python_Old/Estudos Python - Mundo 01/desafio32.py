ano = int(input('Digite um ano e eu irei te dizer se ele é ou não bissexto: '))
if ano % 100 != 0:
    ano % 4 == 0
    ano % 400 == 0
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
