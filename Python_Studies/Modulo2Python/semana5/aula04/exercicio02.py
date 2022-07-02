def stringer(func):
    
    def inverter(str, num):
        # Podendo passar o numero de vezes que desejar
        return str[::-1] * num
    
    return inverter

@stringer
def funcao_chama(str):
    return str

teste_1 = funcao_chama("Breno", 5)
print(teste_1)
