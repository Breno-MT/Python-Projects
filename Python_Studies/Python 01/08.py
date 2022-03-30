############################# function = um block of code no qual é executado
############################# quando chamado

# def hello(primeiro_nome, sobrenome, idade):
    # print(f"Olá! {primeiro_nome} {sobrenome}, você tem {idade} anos!")
    # print("Tenha um ótimo dia!")

# hello("João", "Carvalho", 31)

############################# return statement = funções que manda Valores/Objetos Python de volta para o chamador.
############################# Estes valores/objetos são conhecidos como funções de retorno de valor.

#def multiply(number1, number2):
    #return number1 * number2
#x = multiply(6,8)

#print(x)

############################# keyword arguments = argumentos precedidos por um identificador quando nós passamos a eles uma função
############################# A ordem dos argumentos não importa, diferente de argumentos posicionais.
############################# Python sabe o nome dos argumentos que nossas funções recebem

#def hello(first, middle, last):
    #print("Hello {} {} {}" .format(first,middle,last))
#hello(middle="Martins", last="Teixeira", first="Breno")

############################# nested functions calls = a função de dentro chama outra função.
############################# a mais profunda função que é chamada, são resolvidas primeiro
############################# valor retornado é usado como argumento
#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs((float(input("Enter a whole positive number: "))))))