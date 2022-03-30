i = 1
while i <= 6:
    print(i)
    i += 1

#saindo de um loop mesmo qnd a condição é verdadeira
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#utilizando o continue - para e continua aqui
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
