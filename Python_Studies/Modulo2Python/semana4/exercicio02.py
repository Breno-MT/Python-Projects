class Funcionario():
    def __init__(self, nome, salario = 3500, empregado = True):
        self.nome = nome
        self.salario = salario
        self.empregado = empregado
    
    def setar_salario(self):
        salario = 5000
    
    def aumentar_salario(self, porcentagem):
        self.porcentagem = porcentagem

        aumento = self.salario * porcentagem/100
        self.salario = self.salario + aumento
    
    def demitir(self):
        self.empregado = False
        print("O empregado está demitido!")

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, empregado):
        super().__init__(nome, salario, empregado)

class Designer(Funcionario):
    def __init__(self, nome, salario, empregado):
        super().__init__(nome, salario, empregado)

class Gerente_Marketing(Funcionario):
    def __init__(self, nome, salario, empregado):
        super().__init__(nome, salario, empregado)
    
    def bonificacao(self, porcentagem):

        if self.empregado == False:
            print("Você não pode receber bonus! Pois está demitido!")
        
        else:
            aumento = self.salario * porcentagem/100
            self.salario = self.salario + aumento
            print("Parabéns pelo bonus!")

func = Gerente_Marketing("Breno", 5000, True)
func_1 = Desenvolvedor("Brenin", 2500, True)

print("-*-"*10)
print("Salario atual!")
print(func_1.salario)

print("-*-"*10)
print("Salario aumentado!")

func_1.aumentar_salario(35)
print(func_1.salario)
print(func_1.empregado)

print("-*-"*10)
print("Bonus de venda!")
print(f"Salario atual com bonus!")
func.bonificacao(15)
print(func.salario)

print("-*-"*10)
print("Demitido!")
func_1.demitir()
print(func_1.empregado)
