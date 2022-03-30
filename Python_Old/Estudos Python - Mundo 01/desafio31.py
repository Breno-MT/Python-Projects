km = int(input('Qual a distância da sua viagem até o destino?: '))
if km <=200:
    va = km * 0.50
    print('Você irá pagar um total de: R${:.2f}' .format(va))
else:
    km >200
    vb = (km - 200) * 0.45
    print('Você irá pagar um total de: R${:.2f}' .format(vb))
