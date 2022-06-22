# Construir aplicação de venda de passagens de um ônibus com 46 lugares, o menu da aplicação deve conter os seguintes itens: 

# Comprar Passagem (Mostrar apenas caso ainda não tenha comprado)
# Cancelar Passagem (Mostrar quando tiver poltrona selecionada)
# Alterar Poltrona (Caso já tenha poltrona escolhida) 
# Sair

# 	As propriedades de valor da compra e poltrona devem ser construídas com encapsulamento,
#   não permitindo que o cliente altere diretamente o valor da variável. Ao final da aplicação, 
#   informar qual poltrona o usuário selecionou e o valor total da compra ou mostrar que a compra foi cancelada sem custo.


class Passagens:

    def __init__(self, nome):
        self.nome = nome
        self.__preco_passagem = 99.90
        self.__lugar_passagem = [x+1 for x in range(0,45)]


    @property
    def comprarPassagem(self):
        
        opcao = str(input(f"""
        Olá, o valor da passagem é de R${self.__preco_passagem}
        Temos disponível no total de {len(self.__lugar_passagem)} lugares!
        
        Deseja comprar? (s/n):
        -> """))

        if opcao.lower() == 'sim':
            
            global assento_comprada
            assento_comprada = int(input("De 1 a 46, qual o número que você quer da seu assento?: "))
            
            if assento_comprada > 46:
                print("Digite apenas até o número 46!")
            
            elif assento_comprada < 1:
                print('Digite acima do número 1!')

            print(f"Você comprou o assento na posição {assento_comprada}, obrigado {self.nome} !")
            self.__lugar_passagem.remove(assento_comprada)
            return self.__lugar_passagem

        if opcao.lower() == 's':
            assento_comprada = int(input("De 1 a 46, qual o número que você quer da seu assento?: "))
            
            if assento_comprada > 46:
                print("Digite apenas até o número 46!")
            
            elif assento_comprada < 1:
                print('Digite acima do número 1!')

            print(f"Você comprou o assento na posição {assento_comprada}, obrigado {self.nome} !")
            self.__lugar_passagem.remove(assento_comprada)
            print(f"Lugares disponíveis restantes! {self.__lugar_passagem}")
        
        if opcao.lower() == 'não':
            print("Você não comprou!")
        if opcao.lower() == 'nao':
            print("Você não comprou!")
        if opcao.lower() == 'n':
            print("Você não comprou!")
    
    @property
    def alterarPoltrona(self):
        print(f"Os assentos disponíveis para troca são: {self.__lugar_passagem} !")
        assento_alterado = int(input("Digite o número do assento desejado: "))

        self.__lugar_passagem.append(assento_comprada)
        self.__lugar_passagem.remove(assento_alterado)
        print(f"Assentos disponíveis atualmente são {self.__lugar_passagem}")
    
    @property
    def cancelarPassagem(self):
        print(f"Você cancelou sua compra do assento {assento_comprada}! E o valor de R${self.__preco_passagem} foi retornado.")
        self.__lugar_passagem.append(assento_comprada)
        print(f"Lista de passagem disponiveis: {self.__lugar_passagem}")

comprador = Passagens('Breno')

while True:
    opcao = int(input(""" Bem-vindo(a)!
    [1] Comprar Passagem
    [2] Cancelar Passagem
    [3] Alterar Passagem
    [0] Sair

    Digite sua opção: """))

    if opcao == 1:
        opcao = comprador.comprarPassagem

    elif opcao == 2:
        opcao = comprador.cancelarPassagem

    elif opcao == 3:
        opcao = comprador.alterarPoltrona

    elif opcao == 0:
        break
