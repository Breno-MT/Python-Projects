# Método Closure

def media(num):
    
    def soma(x,y):
        return (x + y) / num
    return soma


test_1 = media(2)

print(test_1(5,5))
###################


# High-order function

def calcular(funcao):
    return funcao

def media(x,y):
    return (x + y) / 2

print(calcular(media(5,5)))
