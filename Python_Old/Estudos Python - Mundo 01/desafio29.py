km = int(input('Qual a velocidade do seu carro?: '))
if km <= 80:
    print('')
else:
    km >= 80
    multa = (km - 80) * 7
    print('Você foi multado em R${:.2f}! Contate o Detran para saber mais!' .format(multa))
