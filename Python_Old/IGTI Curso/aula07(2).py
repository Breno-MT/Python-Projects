#seja esta função
def minha_função():
    variavel_interna = 300
    print(variavel_interna)

minha_função()

#acessando a variavel dentro de outra função
def minha_função():
    variavel_interna = 300
    def minha_função_interna():
        print(variavel_interna)
    minha_função_interna()

minha_função()