import random

class Garcom:
    def __init__(self, nome = "Juninho"):
        self.nome = nome

class Pizza:
    def __init__(self,tamanho, preco, sabor = "4 Queijos"):
        self.tamanho = tamanho
        self.preco = preco
        self.sabor = sabor

class Cliente:
    def __init__(self,nome, mesa = 1, valorGasto = 0):
        self.nome = nome
        self.mesa = mesa
        self.valorGasto = valorGasto

    def soma_valor(self, valor):
        self.valorGasto += valor

class Pedido:
    def __init__(self,codigo, mesa, valor, nomeCliente, nomeGarcom):
        self.codigo = codigo
        self.mesa = mesa
        self.valor = valor
        self.nomeCliente = nomeCliente
        self.nomeGarcom = nomeGarcom

pizza_1 = Pizza("P", 30.99)
pizza_2 = Pizza("M", 40.90)
pizza_3 = Pizza("G", 65.35)

garcom = Garcom()

cliente = Cliente("Breno")

pedidos = []

while True:
    pizzaPedido = int(input(f"""
        Realizar pedido de pizza para o Cliente {cliente.nome}, Mesa {cliente.mesa}

        [1] - Pizza P
        [2] - Pizza M
        [3] - Pizza G
        --------------
        [0] Sair

    """))

    if pizzaPedido == 1:
        preco = pizza_1.preco

    elif pizzaPedido == 2:
        preco = pizza_2.preco

    elif pizzaPedido == 3:
        preco = pizza_3.preco
    
    elif pizzaPedido == 0:
        break

    cliente.soma_valor(preco)

    pedidos.append(
        Pedido(random.randint(0,100), cliente.mesa, preco, cliente.nome, garcom.nome)
    )

print(f"""O cliente {cliente.nome} gastou R${cliente.valorGasto:.2f}! 
    Mesa: {cliente.mesa}
    Pedido: {pedidos[0].codigo}
""")