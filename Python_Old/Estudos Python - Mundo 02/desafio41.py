from datetime import date
atual = date.today().year
nasc = int(input('Olá, digite sua data de nascimento: '))
idade = atual - nasc
print('Verificando categorias...')
if 0 <= idade <=9:
    print('De acordo com sua idade, você pertence a categoria \033[36mMIRIM\033[m!')
if 10 <= idade <=14:
    print('De acordo com sua idade, você pertence a categoria \033[33mINFANTIL\033[m!')
if 15 <= idade <=19:
    print('De acordo com sua idade, você pertence a categoria \033[35mJUNIOR\033[m!')
elif idade == 20:
    print('De acordo com sua idade, você pertence a categoria \033[32mSÊNIOR\033[m!')
elif idade >20:
    print('De acordo com sua idade, você pertence a categoria \033[31mMASTER\033[m!')
