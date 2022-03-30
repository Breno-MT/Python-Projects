variavel_externa = 300
def minha_função():
    print(variavel_externa)

minha_função()

print(variavel_externa)

#modificando variáveis globais
variavel = 300
def minha_funcao():
    variavel = 200
    print(variavel)

minha_funcao()
print(variavel)

#utilizando a palavra global
def minha_função():
    global variavel_global
    variavel_global = 300
minha_função()

print(variavel_global)

#trocando o valor de varia'vel global dentro da função altera o valor da variável
x = 300

def minha_função():
    global x
    x = 200
minha_função()
print(x)