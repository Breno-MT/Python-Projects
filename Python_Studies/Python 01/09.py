############################# Scope = A região na qual a variavel é reconhecivel
############################# A variavel esta apenas disponivel de dentro da região na qual foi criado
############################# A versões de Scope global e local podem ser criadas

#name = "Breno" # Exemplo de Scope Global, está disponivel dentro e fora de funções

#def display_name():
    #name = "Bro" # Exemplo de Scope local, está apenas disponivel dentro dessa função
    #print(name)

#display_name()
#print(name)


############################# *args = um parametro que irá empacotar todos os argumentos na tuple
############################# util para que uma função possa aceitar varios argumentos 

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7))
