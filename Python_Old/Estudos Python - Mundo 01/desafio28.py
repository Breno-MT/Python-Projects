from random import randint
ran = randint(0,5)
num = int(input('Digite um número de 0 a 5: '))
if num == ran:
    print('Parabéns! Você acertou o número!')
else:
    print('Você errou! O número era {}! Tente novamente!'.format(ran))
