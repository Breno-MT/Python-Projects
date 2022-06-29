class Cliente:

    def __init__(self, nome: str):
        self.nome = nome
        self.enderecos = []

    def cadastrar_endereco(self, cidade: str, estado: str):
        self.enderecos.append(Endereco(cidade = cidade, 
                              estado = estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f"O cliente {self.nome}, reside em: {endereco.cidade}-{endereco.estado}")

class Endereco:
    
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


cliente_1 = Cliente("Breno")
cliente_1.cadastrar_endereco("Florianópolis", "SC")
cliente_1.listar_enderecos()
