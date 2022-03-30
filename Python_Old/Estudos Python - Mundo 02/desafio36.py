casa = float(input('Olá, qual o valor da casa: R$ '))
salario = float(input('Agora o seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar a casa: '))
prestaçao = casa / (anos * 12)
print('Para pagar uma Casa de R${:.2f} em {} anos, a prestação será de R${:.2f}!'.format(casa, anos, prestaçao))
if prestaçao > (salario *0.3):
    print('Infelizmente o preço excede o limite de 30% do seu salário! Portanto, a operação será negada.')
else:
    print('Seu empréstimo está aprovado! Tenha uma boa sorte! Qualquer dúvida chamar a corredoria.')
