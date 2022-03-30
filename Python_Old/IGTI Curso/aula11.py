#def concatena_nome_mensagem(nome, mensagem):
    #print('Olá,', nome + '! ' + mensagem)

#concatena_nome_mensagem('Maria', 'Bom Dia!')

#exemplo de função
def concatena_nome_mensagem(nome, mensagem='Bom dia!'):
    print('Olá,', nome + '! ' + mensagem)
#chamando a função apenas com 1 argumento
concatena_nome_mensagem('Maria')

#exemplo de função
def concatena_nome_mensagem(nome, mensagem):
    print('Olá,', nome + '! ' + mensagem)
#chamando a função corretamente
concatena_nome_mensagem('Maria', 'Bom Dia!')

#exemplo de função
def print_nomes_dos_usuarios(*nomes):  #a função possui n parâmetros
    for nome in nomes:
        print('Olá, ' +nome+'! Bom dia!')

print_nomes_dos_usuarios('Maria', 'Antônio', 'José', 'Túlio', 'Breno')

#como o python faz isso
def minha_função(**kwargs):
    print(str(kwargs))

minha_função(a=12, b='abc')

{'a': 12, 'b': 'abc'}

#definição com a posição e apenas 2 valores
def somatorio(a, b):
    print('Somatório é : ', a + b)
    
somatorio(21, 5)
# se colocarmos 3 argumentos, vai dar erro.

#definição com o *args
def somatorio(*args):
    total = 0;
    for arg in args:
        total += arg
    print('Somatório é : ', total)

somatorio(21,5,6)