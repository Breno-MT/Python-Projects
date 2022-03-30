############################# nested loops = um loop dentro de outro loop

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

############################# Controle de Condições de Loop = muda a execução do loop da sua sequência normal
# break = é usado para terminar com o loop todo.
# continue = pula para a proxima iteração do loop
# pass = faz nada, é igual a nada.

#Break exemplo\/
#while True:
    #name = input("Enter your name: ")
    #if name != "":
        #break

#Continue exemplo \/
#phone_number = "123-456-7890"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

#Pass exemplo\/
#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i)
