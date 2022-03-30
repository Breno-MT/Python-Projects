num1 = int(input('Digite o primeiro número INTEIRO: '))
num2 = int(input('Digite o segundo número INTEIRO: '))
if num1 > num2:
    print('O maior valor é \033[31m{}\033[m! E o segundo maior é \033[36m{}\033[m! '.format(num1, num2))
elif num2 > num1:
    print('O maior valor é \033[31m{}\033[m! E o segundo maior é \033[36m{}\033[m!'.format(num2, num1))
else:
    print('Não existe um valor maior que o outro, ambos são iguais!')
