set1 = {1,2,3}

print(set1)

# # adiciona um elemento
set1.add(6)
set1.add(39)
print(set1)

# # adiciona mais de 1 elemento
set1.update([4,5,7])

set_sorted = sorted(set1)

print(set_sorted)

# # remove algum valor especifico do set, mas se não houver vai retornar erro
set1.remove(1)
print(set1)


lista = [5,3,5,2]

print(set(lista))


