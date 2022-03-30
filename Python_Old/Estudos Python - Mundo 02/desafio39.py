from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ANO de nascimento: '))
idade = atual - nascimento
tempo = 18 - (atual - nascimento)
tempo2 = (atual - nascimento) - 18
print('Sistema analisando...')
if idade <18:
    print('Ainda não chegou sua hora de se alistar! Faltam {} ano(s)!'.format(tempo))
elif idade == 18:
    print('Já está na hora de se alistar! Você está atrasado!')
else:
    print('Você já passou do tempo do alistamento! Você está {} ano(s) atrasado!'.format(tempo2))
