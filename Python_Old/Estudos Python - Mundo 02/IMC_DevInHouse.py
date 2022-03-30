# Irá pegar o peso da pessoa.
peso = float(input('Digite o seu peso(KG): '))

# Irá pegar a altura da pessoa em metros.
altura = float(input('Digite sua altura em METRO(m) Exemplo>"1.85": '))

# A Variavel m é o resultado entre o peso dividido pela altura elevada ao quadrado.
# Que será usada para verificar se a pessoa está acima, abaixo etc... do peso dela.
m = peso / (altura * altura)

# Aqui abaixo são as condições de acordo com o resultado da pessoa.
if m <18.5:
    print('Você está com {:.1f} de peso! '.format(m), end='')
    print('Está abaixo do peso! Consulte um nutricionista!')
elif 18.6<= m <=25.9:
    print('Você está com {:.1f} de peso! '.format(m), end='')
    print('Está no peso ideal.')
elif 26<= m <=30.9:
    print('Você está com {:.1f} de peso! '.format(m), end='')
    print('Está com sobrepeso! Consulte um nutricionista!')
elif 31<= m <=40:
    print('Você está com {:.1f} de peso! '.format(m), end='')
    print('Está com obesidade! Consulte um médico!')
elif m > 40:
    print('Você está com {:.1f} de peso! '.format(m), end='')
    print('Está com obesidade mórbida! Consulte URGENTE um médico!')