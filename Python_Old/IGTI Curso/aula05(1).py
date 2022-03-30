lista_1 = [1,2,3,4,5,6]
lista_2 = [6,7,8,9]
for item in lista_1:
    if item in lista_2:
        print(str(item)+ ' é comum às duas listas.')
    else:
        print(str(item)+ ' não é comum às duas listas.')
