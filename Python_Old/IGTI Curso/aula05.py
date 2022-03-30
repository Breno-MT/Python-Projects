lista_de_compras = ['detergente', 'sabão', 'amaciante', 'tomate', 'batata']
item = input('Entre com um produto: ')
if item not in lista_de_compras:
    print('{} não consta na lista de compras.'.format(item))
else:
    print('Não esqueça de comprar {}.'.format(item))
