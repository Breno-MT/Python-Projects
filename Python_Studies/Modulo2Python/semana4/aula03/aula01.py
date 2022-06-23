class Pessoa():
    def __init__(self) -> None:
        pass

    def retornaCidade(self):
        print('Cidade')
    
    @staticmethod
    # poderia funcionar sem o static, apenas retirando o self.
    def temSUS():
        print('Tem sus')
Pessoa.temSUS()  
# p = Pessoa()
# p.retornaCidade()
# p.temSUS()