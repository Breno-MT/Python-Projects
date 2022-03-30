nome = str(input('Qual é o seu nome?: '))
if nome == 'Breno':
    print('Que nome bonito! Poucas pessoas tem a sorte de ter um nome tão belo e lindo como o seu! Parabéns!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem comum no Brasil, que pena de você! Hahaha!')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Que nomes bonitos para um mulherão como você! Hahahaha!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}{}{}!'.format('\033[4;35;47m' , nome, '\033[m'))
