def stringer(func):
    
    def inverter(str):
        return str[::-1]
    
    return inverter

@stringer
def funcao_chama(str):
    return str

teste_1 = funcao_chama("Breno")
print(teste_1)
