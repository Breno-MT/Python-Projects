salario = int(input('Digite o seu salário para calcular o seu aumento: '))
if salario >1.250:
    au1 = salario * 10/100
    sal1 = au1 + salario
    print('O aumento do seu salário é de R${:.2f}! Num total de R${:.2f}!' .format(au1, sal1))
else:
    salario <=1.250
    au2 = salario * 15/100
    sal2 = au2 + salario
    print('O aumento do seu salarial é de R${:.2f}! Num total de R${:.2f}!' .format(au2, sal2))
