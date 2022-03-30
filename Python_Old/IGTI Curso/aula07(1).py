#Qual será o nome da minha função? O nome deve fazer sentido. Mostrar o que será
#executado.
#Quais argumentos a função deve receber? Definir quais valores devem ser passados
#para a função.
#O que a função deve fazer? Deve definir o papel da função em nosso programa,ou seja,
#o que ela deve fazer com os valores passados.
#O que a função deve retornar? Após realizar o processamento, qual o valor
#esperamos receber da função?

#escreva uma função que retorne o valor absoluto de um número
# 1 - o nome da função será valor_absoluto
# 2 - a função vai receber um número (inteiro ou float)
# 3 - a função deve calcular o valor absoluto do número passado
# 4 - a função deve retornar o valor absoluto
def valor_absoluto(num):
    """Esta função retorna o valor
    absoluto de um número"""

    if num >= 0:
        return num
    else:
        return - num
print(valor_absoluto(20))
print(valor_absoluto(-4.5))
