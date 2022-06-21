class Conta:
    def __init__(self, nome, agencia, conta):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        raise ValueError ("Impossível alterar saldo diretamente. Use a função depositar() ou sacar()")
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        
        if valor > self.__saldo:
            print("O valor de saque é maior que tem na conta.")
        else:
            self.__saldo -= valor



conta = Conta('Breno', "0001", '1234')
conta.depositar(1555)
print(f"O saldo da conta do Breno é R${conta.saldo:.2f}")

conta.sacar(1555)
print(f"O saldo da conta atual é R${conta.saldo:.2f}")
