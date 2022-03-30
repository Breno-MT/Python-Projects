def verifica_divisibilidade(x, y):
    x_divisivel_y = False

    if x % y ==0:
        x_divisivel_y = True
    return x_divisivel_y
x = int(input('Entre com um valor inteiro: '))
y = int(input('Entre com outro valor inteiro: '))
 
if verifica_divisibilidade(x,y):
    print(x,' é divisivel por ', y)
else:
    print(x,' não é divisivel por ', y)

#Código mais elegante

def verifica_divisibilidade(x, y):
    return x % y ==0
x = int(input('Entre com um valor inteiro: '))
y = int(input('Entre com outro valor inteiro: '))
 
if verifica_divisibilidade(x,y):
    print(x,' é divisivel por ', y)
else:
    print(x,' não é divisivel por ', y)