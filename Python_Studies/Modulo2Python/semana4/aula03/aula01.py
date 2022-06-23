# class Pessoa():
#     def __init__(self) -> None:
#         pass

#     def retornaCidade(self):
#         print('Cidade')
    
#     @staticmethod
#     # poderia funcionar sem o static, apenas retirando o self.
#     def temSUS():
#         print('Tem sus')
# Pessoa.temSUS()  
# p = Pessoa()
# p.retornaCidade()
# p.temSUS()

class Peso():
    def __init__(self, peso):
        self.peso = peso
    
    def __str__(self) -> str:
        pass

    def __lt__(a, b):
        return a.peso < b.peso

a = Peso(50)
b = Peso(60)

print( a > b )

