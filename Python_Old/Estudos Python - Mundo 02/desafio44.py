print('{:=^40}'.format('LOJA INFO'))
print('Você está perto de comprar o seu TECLADO BLACKWIDOW!')
valor = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
digito = int(input('Qual a forma de pagamento?: '))
if digito == 1:
    total = valor - (valor * 10/100 )
elif digito == 2:
    total = valor - (valor * 5/100)
elif digito == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcela))
elif digito == 4:
    total = valor + (valor * 20/100)
    totalparce = int(input('Quantas parcelas?: '))
    parcela = total / totalparce
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(totalparce, parcela))
else:
    total = valor
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE\033[m!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
