# list = [1,2,3,4,5]

# list.remove(1)

# print(list)

# print('--- apos append')

# list.append("comida")
# print(list)

# while True:
#     palavra = input("Digite uma palavra: ")

#     if palavra.lower() == "sair":
#         print("Fim")
#         break

#     if len(palavra) < 2:
#         print("Palavra muito pequena.")


class Matematica:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def soma(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def multiplicacao(self):
        return self.a * self.b

conta1 = Matematica(5,25)
print(conta1.soma())