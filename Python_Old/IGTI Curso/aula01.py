try:
    n1 = int(input('Digite um valor: '))
    if n1 == 0:
        print('Numerador não pode ser zero.')
        exit(0)
except ValueError:
    print('O número não pode ser float.')
    exit(0)
try:
    n2 = int(input('Digite o segundo valor:'))
except:
        print('Digite APENAS números inteiros.')
        exit(0)
try:
    if n1 % n2 ==0:
        print('O número digitado é divisivel.')
    else:
        print('O numero não é divisivel.')
except ZeroDivisionError:
    print('O segundo número não pode ser zero.')
    